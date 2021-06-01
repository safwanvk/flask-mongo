from flask import  jsonify, request,make_response
from flask_restful import Resource
from model import *
from utils import *

from bson.objectid import ObjectId


class MoviesApi(Resource):
  def get(self):
    try:
      filter = request.args.get('filter')
      if filter:
        movie = db_operations.find_one({'_id' : ObjectId(filter)})
        data = {'Name' : movie['name'], 'Casts' : movie['casts'], 'Genres': movie['genres']}
        return make_response(jsonify({'msg':'Success','data':data}), 200)

      movies = db_operations.find()
      data = [{'Name' : movie['name'], 'Casts' : movie['casts'], 'Genres': movie['genres']} for movie in movies]
      return make_response(jsonify({'msg':'Success','data':data}), 200)
    except Exception as e:
      print(e)
      return None

  def post(self):
    body = request.get_json()
    db_operations.insert_one(body)
    return make_response(jsonify({'msg':'Success'}), 200)

  


class MovieApi(Resource):
  def put(self, id):
    body = request.get_json()
    db_operations.update_one({'_id': ObjectId(id)}, {'$set':body})

    return make_response(jsonify({'msg':'Success'}), 200)

  def get(self, id):
    movie = db_operations.find({'_id' : ObjectId(id)})
    data = {'Name' : movie['name'], 'Casts' : movie['casts'], 'Genres': movie['genres']}
    return make_response(jsonify({'msg':'Success','data':data}), 200)

  def delete(self, id):
    movie = db_operations.delete_one({'_id' : ObjectId(id)})
    return make_response(jsonify({'msg':'Success'}), 200)




class MovieBulkUpload(Resource):
  def post(self):
    body = request.get_json()
    db_operations.insert_many(body.get('data'))
    return {'result' : 'Created successfully'}, 200


#Bulk Update
# db_operations.update_many()


#many delete
# db_operations.delete_many()
