from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Get from environment
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB')

# Initialize MongoDB client once
client = MongoClient(MONGO_URI)

# Select your database
db = client[MONGO_DB]

# Ensure 'data' collection exists or create it
if 'data' not in db.list_collection_names():
    db.create_collection('data')

# Collections you will use
data_collection = db['data']
responses_collection = db['responses']
