from flask import Flask, request, Response
from database.db import initialize_db
from database.models import *

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie'
}

initialize_db(app)




if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')