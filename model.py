from flask_pymongo import PyMongo
from flask import Flask


app = Flask(__name__)



app.config["MONGO_URI"] = "mongodb://localhost:27017/movie"

mongo = PyMongo(app)

#db_operations = mongo.db.<COLLECTION_NAME>
db_operations = mongo.db.Movie