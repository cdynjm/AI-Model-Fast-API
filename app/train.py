# app/train.py

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from database.db import data_collection


def train_model():
    try:
        # Fetch docs from MongoDB
        docs = list(data_collection.find({}, {"_id": 0, "text": 1, "label": 1}))
        if not docs:
            print("⚠️ No training data found.")
            return

        df = pd.DataFrame(docs)
        print("📄 Data sample:")
        print(df.head())

        # Train vectorizer and model
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(df['text'])

        model = LogisticRegression()
        model.fit(X, df['label'])

        # Ensure 'models' folder exists
        models_dir = os.path.join(os.path.dirname(__file__), "..", "models")
        os.makedirs(models_dir, exist_ok=True)

        # Save model & vectorizer
        model_path = os.path.join(models_dir, 'chatbot_model.joblib')
        vectorizer_path = os.path.join(models_dir, 'vectorizer.joblib')

        joblib.dump(model, model_path, compress=3, protocol=4)
        joblib.dump(vectorizer, vectorizer_path, compress=3, protocol=4)

        print(f"✅ Training complete. Files saved to {models_dir}")

    except Exception as e:
        print(f"❌ Error during training: {e}")

train_model()
