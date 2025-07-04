import os
import traceback
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import random

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

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" in request body'}), 400
    input_text = data['text']

    try:
        X = vectorizer.transform([input_text])
        label = model.predict(X)[0]
        response = get_response(label)
    except Exception:
        with open('error.log', 'a') as f:
            f.write("\nError during prediction:\n")
            f.write(traceback.format_exc())
        return jsonify({'error': 'Internal server error during prediction'}), 500

    return jsonify({'response': response})


