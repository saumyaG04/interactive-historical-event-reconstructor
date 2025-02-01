import pymongo
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")  # Default to localhost if not set

# Function to get the database connection
def get_db():
    client = pymongo.MongoClient(MONGO_URI)
    db = client.historyDB  # Connect to the 'historyDB' database
    return db
