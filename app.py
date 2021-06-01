
from flask_pymongo import PyMongo
from movie import *
from flask_restful import Api
from model import *

api = Api(app)


api.add_resource(MoviesApi, '/api/movies')
api.add_resource(MovieApi, '/api/movies/<id>')
api.add_resource(MovieBulkUpload, '/api/movies_bulk')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')