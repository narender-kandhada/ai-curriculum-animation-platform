from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB (use env var if set, fallback to localhost)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URI)

# Database and collection
db = client["animation_app"]
collection = db["stories"]

def save_data(text, script):
    collection.insert_one({
        "text": text,
        "script": script
    })