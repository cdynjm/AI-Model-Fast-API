from pymongo import MongoClient

# Initialize MongoDB client once
client = MongoClient(
    "mongodb+srv://cdynjm:xxSn3JXb0CkbN5BS@cluster1.ziep46f.mongodb.net/myappdb"
    "?retryWrites=true&w=majority&appName=Cluster1"
)

# Select your database
db = client['myappdb']

# Ensure 'data' collection exists or create it
if 'data' not in db.list_collection_names():
    db.create_collection('data')

# Collections you will use
data_collection = db['data']
responses_collection = db['responses']