from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB')

client = MongoClient(MONGO_URI)

db = client[MONGO_DB]

if 'datas' not in db.list_collection_names():
    db.create_collection('datas')

data_collection = db['datas']
responses_collection = db['responses']
