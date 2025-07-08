import os
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def train_model():
    try:
        # Adjust path: data.json is in root folder (one level up from app/)
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        json_dir = os.path.join(root_dir, "json")
        data_json_path = os.path.join(json_dir, "data.json")
        
        # Load data from JSON file
        with open(data_json_path, "r", encoding="utf-8") as f:
            docs = json.load(f)
        
        if not docs:
            print("⚠️ No training data found in data.json.")
            return
        
        # Convert to DataFrame
        df = pd.DataFrame(docs)
        
        print("📄 Data sample:")
        print(df.head())
        
        # Train vectorizer and model
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(df['text'])
        
        model = LogisticRegression()
        model.fit(X, df['label'])
        
        # Save models to root/models folder
        models_dir = os.path.join(root_dir, "models")
        os.makedirs(models_dir, exist_ok=True)
        
        model_path = os.path.join(models_dir, 'chatbot_model.joblib')
        vectorizer_path = os.path.join(models_dir, 'vectorizer.joblib')
        
        joblib.dump(model, model_path, compress=3, protocol=4)
        joblib.dump(vectorizer, vectorizer_path, compress=3, protocol=4)
        
        print(f"✅ Training complete. Files saved to {models_dir}")
        
    except Exception as e:
        print(f"❌ Error during training: {e}")

if __name__ == "__main__":
    train_model()
