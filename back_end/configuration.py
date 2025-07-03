from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("DB_URL")

client = MongoClient(uri, server_api=ServerApi('1'))

db = client[os.getenv("DB_NAME")]
news_collection = db["news"]