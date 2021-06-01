from flask import Flask, request, Response
from database.db import initialize_db
from database.models import *

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie'
}

initialize_db(app)

@app.route('/movies', methods=['POST'])
def add_movie():
    try:
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {'id': str(id)}, 200
    except Exception as e:
        print(e)
        return {'msg':'error'}


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')