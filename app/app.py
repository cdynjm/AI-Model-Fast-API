import os
import shutil
import traceback
import json
import random
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
from app.train import train_model

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(base_dir)
json_dir = os.path.join(project_root, 'json')

app = Flask(__name__, template_folder=os.path.join(project_root, 'templates'))
CORS(app)

# Load your ML model and vectorizer
try:
    model_path = os.path.join(project_root, 'models', 'chatbot_model.joblib')
    vectorizer_path = os.path.join(project_root, 'models', 'vectorizer.joblib')
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except Exception:
    with open('error.log', 'w') as f:
        f.write(traceback.format_exc())
    raise

# Load responses.json into memory
try:
    responses_json_path = os.path.join(json_dir, 'responses.json')
    with open(responses_json_path, 'r', encoding='utf-8') as f:
        responses_data = json.load(f)
except Exception:
    with open('error.log', 'a') as f:
        f.write("\nFailed to load responses.json:\n")
        f.write(traceback.format_exc())
    responses_data = []

def get_response(label: str) -> str:
    try:
        # Lookup response in loaded JSON
        doc = next((item for item in responses_data if item['label'] == label), None)
        if not doc:
            doc = next((item for item in responses_data if item['label'] == "fallback"), None)
        if not doc:
            return "Sorry, I can't respond right now."

        if isinstance(doc['response'], list):
            return random.choice(doc['response'])
        return doc['response']
    except Exception:
        with open('error.log', 'a') as f:
            f.write("\nError in get_response:\n")
            f.write(traceback.format_exc())
        return "Sorry, I can't respond right now."

@app.route('/')
def home():
    title = "Chatbot API"
    message = "The API is running smoothly 🚀"
    return render_template("home.html", title=title, message=message)

@app.route('/train', methods=['GET'])
def train():
    try:
        print("🚀 Starting training process...")

        # Path to your models folder
        models_dir = os.path.join(os.path.dirname(__file__), "..", "models")

        # Delete the entire models folder if it exists
        if os.path.exists(models_dir):
            shutil.rmtree(models_dir)
            print(f"🗑️ Cleared old models at: {models_dir}")

        # Then retrain fresh
        train_model()
        print("✅ Training finished!")

        return jsonify({
            "status": "success",
            "message": "Training complete. Old models cleared."
        }), 200

    except Exception as e:
        print(f"❌ Error during training: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" in request body'}), 400

    input_text = data['text']

    try:
        X = vectorizer.transform([input_text])
        probs = model.predict_proba(X)[0]  # Probabilities for all labels
        max_prob = max(probs)
        label_index = probs.argmax()
        predicted_label = model.classes_[label_index]

        # Fallback if not confident enough
        threshold = 0.2  # Tune this threshold as needed
        if max_prob < threshold:
            predicted_label = "fallback"

        response = get_response(predicted_label)

    except Exception:
        with open('error.log', 'a') as f:
            f.write("\nError during prediction:\n")
            f.write(traceback.format_exc())
        return jsonify({'error': 'Internal server error during prediction'}), 500

    return jsonify({
        'response': response,
        'label': predicted_label,
        'probability': max_prob
    })
