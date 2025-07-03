from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import random

# Import collections from db.py
from db import responses_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText(BaseModel):
    text: str

model = joblib.load('chatbot_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

def get_response(label: str) -> str:
    doc = responses_collection.find_one({"label": label})
    if not doc:
        doc = responses_collection.find_one({"label": "fallback"})
    if isinstance(doc['response'], list):
        return random.choice(doc['response'])
    return doc['response']

@app.post("/chat")
def chat(input: InputText):
    X = vectorizer.transform([input.text])
    label = model.predict(X)[0]
    response = get_response(label)
    return {"response": response}
