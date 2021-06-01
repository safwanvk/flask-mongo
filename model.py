
from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)



app.config["MONGO_URI"] = "mongodb://localhost:27017/movie"

mongo = PyMongo(app)

#db_operations = mongo.db.<COLLECTION_NAME>
db_operations = mongo.db.Movie



from flask import Flask





