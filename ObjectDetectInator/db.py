from flask import Flask
from flask_pymongo import pymongo
connection = "mongodb+srv://PranayVaranasi:789456123eggm%40n0@objectdetectinator.hm51okc.mongodb.net/?retryWrites=true&w=majority&appName=ObjectDetectInator"
client = pymongo.MongoClient(connection)
db = client.get_database('ObjectDetectInator')
collection = pymongo.collection.Collection(db, 'collection')
