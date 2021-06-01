from flask import  jsonify, request,make_response
from flask_restful import Resource
from model import *

class MoviesApi(Resource):
  def get(self):
    try:
      movies = db_operations.find()
      data = [{'Name' : movie['name'], 'Casts' : movie['casts'], 'Genres': movie['genres']} for movie in movies]
      return make_response(jsonify({'msg':'Success','data':data}), 200)
    except Exception as e:
      print(e)
      return None

  def post(self):
    body = request.get_json()
    db_operations.insert_one(body)
    return jsonify({'result' : 'Created successfully'}, 200)


class MovieApi(Resource):
  def put(self, id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200

  def delete(self):
    db_operations.delete_one({'_id':ObjectId('60b5f1f2502eadbd05379293')})
    return '', 200

  def get(self, id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)


class MovieBulkUpload(Resource):
  def post(self):
    body = request.get_json()
    db_operations.insert_many(body.get('data'))
    return {'result' : 'Created successfully'}, 200

