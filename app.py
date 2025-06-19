from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)
app.secret_key = "secretkey"

app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/Users')
mongo = PyMongo(app)

# Create Function(POST /users)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data['name']
    email = data['email']
    password = data['password']
    if name and email and password and request.method == 'POST':
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert_one({'name': name, 'email':email, 'password':hashed_password})
        resp = jsonify("CREATE function executed successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

# Read All Users Function(GET /users)
@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    resp = dumps(users)
    return resp

# Read One User Function(GET /users/<id>)
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp

# Update User Function (PUT /users/<id>)
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    name = data['name']
    email = data['email']
    password = data['password']
    if name and email and password and request.method == 'PUT':
        hashed_password = generate_password_hash(password)
        result = mongo.db.users.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'name': name, 'email': email, 'password': hashed_password}}
        )
        if result.matched_count == 0:
            return not_found()
        resp = jsonify("UPDATE function executed successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

# Delete Function(DELETE /users/<id>)
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    resp = jsonify("DELETE Function executed Successfully")
    resp.status_code = 200
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url
    }
    return jsonify(message), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)