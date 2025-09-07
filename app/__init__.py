import os
import shutil
import traceback
import sys, platform
import json
import random
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
from fuzzywuzzy import fuzz
import re

# -----------------------------
# Paths and directories
# -----------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(base_dir)
json_dir = os.path.join(project_root, 'json')
log_dir = os.path.join(project_root, 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'error.log')

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Optional: log errors to console as well
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logging.getLogger().addHandler(console_handler)

# -----------------------------
# Flask app
# -----------------------------
app = Flask(__name__, template_folder=os.path.join(project_root, 'templates'))
CORS(app)

# -----------------------------
# Load ML model and vectorizer
# -----------------------------
try:
    model_path = os.path.join(project_root, 'models', 'chatbot_model.joblib')
    vectorizer_path = os.path.join(project_root, 'models', 'vectorizer.joblib')
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except Exception as e:
    logging.error("Failed to load model/vectorizer", exc_info=e)
    raise

# -----------------------------
# Load responses.json
# -----------------------------
try:
    responses_json_path = os.path.join(json_dir, 'responses.json')
    with open(responses_json_path, 'r', encoding='utf-8') as f:
        responses_data = json.load(f)
except Exception as e:
    logging.error("Failed to load responses.json", exc_info=e)
    responses_data = []

# -----------------------------
# Prepare fuzzy_questions
# -----------------------------
fuzzy_questions = {}
for item in responses_data:
    label = item.get('label')
    questions = item.get('questions') or item.get('patterns') or []
    if questions and isinstance(questions, list):
        fuzzy_questions[label] = questions

# -----------------------------
# Helper functions
# -----------------------------
def find_labels_multi_intent(input_text):
    labels_found = set()
    parts = [part.strip() for part in re.split(r'\band\b|,|&', input_text.lower())]
    for part in parts:
        best_label = None
        best_score = 0
        for label, examples in fuzzy_questions.items():
            for example in examples:
                score = fuzz.ratio(part, example.lower())
                if score > best_score:
                    best_score = score
                    best_label = label
        if best_score >= 50 and best_label:
            labels_found.add(best_label)
    return list(labels_found)

def get_response(label: str) -> str:
    try:
        doc = next((item for item in responses_data if item['label'] == label), None)
        if not doc:
            doc = next((item for item in responses_data if item['label'] == "fallback"), None)
        if not doc:
            return "Sorry, I can't respond right now."

        if isinstance(doc['response'], list):
            return random.choice(doc['response'])
        return doc['response']
    except Exception as e:
        logging.error("Error in get_response", exc_info=e)
        return "Sorry, I can't respond right now."

# -----------------------------
# Routes
# -----------------------------
@app.route('/')
def home():
    title = sys.version
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
        probs = model.predict_proba(X)[0]
        max_prob = max(probs)
        label_index = probs.argmax()
        predicted_label = model.classes_[label_index]

        threshold = 0.2
        multi_labels = find_labels_multi_intent(input_text)

        if max_prob < threshold or len(multi_labels) > 1:
            if multi_labels:
                responses_combined = [get_response(lbl) for lbl in multi_labels]
                response = " ".join(responses_combined)
                predicted_label = ", ".join(multi_labels)
            else:
                predicted_label = "fallback"
                response = get_response(predicted_label)
        else:
            response = get_response(predicted_label)

    except Exception as e:
        logging.error("Error during prediction", exc_info=e)
        return jsonify({'error': 'Internal server error during prediction'}), 500

    return jsonify({
        'response': response,
        'label': predicted_label,
        'probability': max_prob
    })

# -----------------------------
# Global error handler
# -----------------------------
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error("Unhandled Exception", exc_info=e)
    return "An internal error occurred.", 500
