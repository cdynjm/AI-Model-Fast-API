import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

from db import data_collection

docs = list(data_collection.find({}, {"_id": 0, "text": 1, "label": 1}))

df = pd.DataFrame(docs)

print(df.head())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])

model = LogisticRegression()
model.fit(X, df['label'])

joblib.dump(model, 'chatbot_model.joblib', compress=3, protocol=4)
joblib.dump(vectorizer, 'vectorizer.joblib', compress=3, protocol=4)

print("✅ Training complete. Model & vectorizer saved with protocol 4.")