import os
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import random

app = Flask(__name__)
CORS(app)  # Enable CORS

# Try to import db and load models, catch errors and log them
try:
    from db import responses_collection

    base_dir = os.path.dirname(os.path.abspath(__file__))
    model = joblib.load(os.path.join(base_dir, 'chatbot_model.joblib'))
    vectorizer = joblib.load(os.path.join(base_dir, 'vectorizer.joblib'))
except Exception:
    with open('error.log', 'w') as f:
        f.write(traceback.format_exc())
    # Re-raise to let Passenger know the app failed
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
        # Log DB errors but return fallback string to avoid crashing
        with open('error.log', 'a') as f:
            f.write("\nDB error in get_response:\n")
            f.write(traceback.format_exc())
        return "Sorry, I can't respond right now."

@app.route('/')
def home():
    return "Flask chatbot API is running!"

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
