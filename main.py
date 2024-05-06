from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import pprint
import os

passwod = os.environ.get("MONGO_PASS")

connection_string = f"mongodb+srv://fozlerabbi190:{passwod}@cluster0.fuu7vqq.mongodb.net/"

client = MongoClient(connection_string)
