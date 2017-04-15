from flask import Flask, jsonify, request
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
	try:
		user = User.create(
			email=str(request.form['email']),
			first_name=str(request.form['first_name']),
			last_name=str(request.form['last_name']),
			password=""
		)
	except:
		return jsonify({'code' : 10000, 'msg' : "Email already exists"}), 409


@app.route('/users/<user_id>', methods=['GET'])
def list_user_by_id(user_id):
	user_ids = []
	for user_id in User.select():
		user_ids.append(user_id.to_hash())
	return jasonify(user_ids)


@app.route('/users/<user_id>', methods=['PUT'])
def update_user_by_id():
	user_ids = []
	for key in request.values:
		if key == 'email':
			return jsonify({'msg' : 'email can not be changed'}), 409
		if key == 'updated_at' or key == 'created_at':
			 continue
		else:
			 setattr(user_ids, key, request.values.get(key))
	user.save()
	return jsonify({'msg' : 'user sucessfuly updated'}), 200


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id():
	user_ids = []
	try:
		for user_id in User.select():
			user_ids.delete_instance()
			users.save()
	return jsonify({'code' : 200, 'msg' : 'success'}), 200
	except:
		return jsonify({'code' : 404, 'msg' : 'not delted'}), 404
