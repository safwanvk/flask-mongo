from flask import Response, request
from flask_restful import Resource
from model import *

class MoviesApi(Resource):
  def get(self):
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json()
    db_operations.insert_one(body)


    return {'result' : 'Created successfully'}, 200

class MovieApi(Resource):
  def put(self, id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200

  def delete(self, id):
    movie = Movie.objects.get(id=id).delete()
    return '', 200

  def get(self, id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)
