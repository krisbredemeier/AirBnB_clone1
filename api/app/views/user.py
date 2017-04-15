from flask import Flask, jsonify
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State



@app.route('/users', methods=['GET'])
def list_users():
	users = []
	for user in User.select():
		users.append(user.to_hash())
	return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
	# TODO
	pass

@app.route('/users/<user_id>', methods=['GET'])
def list_user_by_id(user_id):
	user_id = []
	for user_id in User.select():
		users.append(user_id.to_hash())
	return jasonify(user_id)


@app.route('/users/<user_id>', methods=['PUT'])
def update_user_by_id():
	# TODO
	pass

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id():
	# TODO
	pass
