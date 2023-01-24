from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from controllers import games
from waitress import serve

app = Flask(__name__)
CORS(app)

@app.route("/")
def welcome():
    return jsonify({"message": "Welcome to the game API"})

@app.route("/games", methods = ['GET', 'POST'])
def game():
    fns = {
        'GET': games.index,
        'POST': games.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/games/<int:game_id>', methods = ['GET', 'PATCH', 'PUT', 'DELETE'])
def game_handler(game_id):
    fns = {
        'GET': games.show,
        'PUT': games.update,
        'PATCH': games.update,
        'DELETE': games.destroy
    }
    resp, code = fns[request.method](request, game_id)
    return jsonify(resp), code

serve(app, listen='*:8080')
