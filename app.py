from flask import Flask, request, Response
from database.db import initialize_db
from resources.routes import *
from flask_restful import Api

app = Flask(__name__)

api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie'
}

initialize_db(app)

initialize_routes(api)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')