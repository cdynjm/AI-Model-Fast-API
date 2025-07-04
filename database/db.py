from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB')

client = MongoClient(MONGO_URI)

db = client[MONGO_DB]

if 'data' not in db.list_collection_names():
    db.create_collection('data')

data_collection = db['data']
responses_collection = db['responses']
