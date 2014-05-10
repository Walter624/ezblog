__author__ = 'walter'
from ezblog import app
from pymongo import MongoClient

mongo_client = MongoClient(app.config['MONGO']['HOST'], app.config['MONGO']['PORT'])
db = mongo_client[app.config['MONGO']['DATABASE']]