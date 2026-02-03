from pymongo import MongoClient
from bot.config import MONGO_DB_URI, DB_NAME

mongo = MongoClient(MONGO_DB_URI)
db = mongo[DB_NAME]
