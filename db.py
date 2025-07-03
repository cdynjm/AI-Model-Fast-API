from pymongo import MongoClient

client = MongoClient("mongodb+srv://cdynjm:xxSn3JXb0CkbN5BS@cluster1.ziep46f.mongodb.net/myappdb?retryWrites=true&w=majority&appName=Cluster1")
db = client['myappdb']

data_collection = db['data']
responses_collection = db['responses']