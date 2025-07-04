import os
import shutil
import traceback
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import random
from app.train import train_model

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(base_dir)

app = Flask(__name__, template_folder=os.path.join(project_root, 'templates'))
CORS(app)

try:
    from database.db import responses_collection
    model_path = os.path.join(project_root, 'models', 'chatbot_model.joblib')
    vectorizer_path = os.path.join(project_root, 'models', 'vectorizer.joblib')
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

except Exception:
    with open('error.log', 'w') as f:
        f.write(traceback.format_exc())
    raise

def get_response(label: str) -> str:
    try:
        doc = responses_collection.find_one({"label": label})
        if not doc:
            doc = responses_collection.find_one({"label": "fallback"})
        if isinstance(doc['response'], list):
            return random.choice(doc['response'])
        return doc['response']
    except Exception:
        with open('error.log', 'a') as f:
            f.write("\nDB error in get_response:\n")
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

        # 👇 Fallback if not confident enough
        threshold = 0.2 # Tune this! Try 0.5 ~ 0.7
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



