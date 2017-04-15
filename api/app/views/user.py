from flask import Flask, jsonify, request
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State



@app.route('/users', methods=['GET'])
def list_users():
	'''
	Get all users
	This will list all users in the database
	---
	tags: - User
	responses:
      200:
        description: return list of all users
        schema:
          id: Users
          properties:
		  	users:
              type: array
              description: array of users
	'''
	users = []
	for user in User.select():
		users.append(user.to_hash())
	return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
	'''
	Create a new user
	Creates a new users and appends to database
	---
	tags: - User
	parameters:
		-
			name: email
			in: form
			type: string
			required: True
			description: email of the user

		-
			name: frist_name
			in: form
			type: string
			required: True
			description: first name of the user
		-
			name: last_name
			in: form
			type: string
			required: True
			description: last name of the user
		-
			name: password
			in: form
			type: string
			required: True
			description: password of the user

	responses:
		409:
			description: email already exists
	'''

	try:
		user = User.create(
			email=str(request.form['email']),
			first_name=str(request.form['first_name']),
			last_name=str(request.form['last_name']),
			password=str(request.form['password'])
		)
		return jsonify(user)
	except:
		return jsonify({'code' : 10000, 'msg' : "Email already exists"}), 409


@app.route('/users/<user_id>', methods=['GET'])
def list_user_by_id(user_id):
	'''
	Get user by id
	list of the given user using user_id in databse
	---
	tags: User
	responses:
		404:
		descripton: aboarts route, can not list user by id

	'''
	try:
		user = User.get(User.id == user_id)
        return jsonify(user)
	except:
		abort(404)

@app.route('/users/<user_id>', methods=['PUT'])
def update_user_by_id():
	'''
	Update user
	Updates existing user and appends to database
	---
	tags: - User
	parameters:
	responses:
		409:
			descripton: notify that the email can not be changed
		200:
			descripton: user was sucessfully updated
		404:
			descripton: user was not updated, error occured
	'''
	try:
		user = User.get(User.id == user_id)
		for key in request.values:
			if key == 'email':
				return jsonify({'msg' : 'email can not be changed'}), 409
			if key == 'updated_at' or key == 'created_at':
				 continue
			else:
				 setattr(user, key, request.values.get(key))
		user.save()
		return jsonify(user), 200
	except:
		abort(404)


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id():
		'''
		Delete user
		Removes user specified by id from database
		---
		tags: - User
		parameters:
		responses:
			200:
				descripton: sucessfully deletes ueser
			404:
				descripton: user was not delted from database
		'''
	user = User.get(User.id == user_id)
	try:
		for user in User.select():
			user_ids.delete_instance()
			user.save()
		return jsonify({'msg' : 'success'}), 200
	except:
		return jsonify({'msg' : 'not delted'}), 404
