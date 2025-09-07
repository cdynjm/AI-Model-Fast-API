import os
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def train_model():
    try:
        # Root and JSON directory
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        json_dir = os.path.join(root_dir, "json")
        data_json_path = os.path.join(json_dir, "data.json")
        
        # Load training data
        with open(data_json_path, "r", encoding="utf-8") as f:
            docs = json.load(f)
        
        if not docs:
            print("⚠️ No training data found in data.json.")
            return
        
        # Convert to DataFrame
        df = pd.DataFrame(docs)
        df['text'] = df['text'].astype(str)  # Ensure strings
        
        print("📄 Sample data:")
        print(df.head())
        
        # TF-IDF vectorizer
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(df['text'])
        
        # Logistic Regression model
        model = LogisticRegression(solver='liblinear', max_iter=200)
        model.fit(X, df['label'])
        
        # Save models
        models_dir = os.path.join(root_dir, "models")
        os.makedirs(models_dir, exist_ok=True)
        
        model_path = os.path.join(models_dir, 'chatbot_model.joblib')
        vectorizer_path = os.path.join(models_dir, 'vectorizer.joblib')
        
        # Use compress=3 and protocol compatible with Python 3.7/joblib 0.14
        joblib.dump(model, model_path, compress=3, protocol=4)
        joblib.dump(vectorizer, vectorizer_path, compress=3, protocol=4)
        
        print(f"✅ Training complete. Files saved to {models_dir}")
        
    except Exception as e:
        print(f"❌ Error during training: {e}")
        with open(os.path.join(root_dir, 'error.log'), 'a') as f:
            f.write(f"\nError during training:\n{str(e)}\n")

if __name__ == "__main__":
    train_model()
