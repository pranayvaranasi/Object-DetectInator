from flask import Flask
from flask_pymongo import pymongo
connection = #hidden for privacy reasons
client = pymongo.MongoClient(connection)
db = client.get_database('ObjectDetectInator')
collection = pymongo.collection.Collection(db, 'collection')
