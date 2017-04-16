from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State



@app.route('/users', methods=['GET'])
def list_users():
	"""
	Get all users
	This will list all users in the database
	---
	tags:
		- user
	responses:
		200:
			description: return list of all users
			schema:
				type: array
				items:
					$ref: '#/definitions/User'
	"""
	users = []
	for user in User.select():
		users.append(user.to_hash())
	return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
	"""
	Create a new user
	Creates a new users and appends to database
	---
	tags:
		- user
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
		200:
			description: the User representation
			schema:
				id: User
				properties:
					id:
						type: number
						description: Unique identifier
						required: true
					created_at:
						type: date-time
						description: Datetime of the item creation
						required: true
					updated_at:
						type: date-time
						description: Datetime of the last item update
						required: true
					email:
						type: string
						description: Email of the user
						required: true
					first_name:
						type: string
						description: First name of the user
						required: false
					last_name:
						type: string
						description: Last name of the user
						required: false
					password:
						type: string
						description: Password of the user, MD5 encoded
						required: true
					is_admin:
						type: boolean
						description: Define if the user is admin
						required: true
		409:
			description: email already exists
	"""

	try:
		user = User(
			first_name=str(request.form['first_name']),
			last_name=str(request.form['last_name']),
			email=str(request.form['email']),
			is_admin=False,
			password=str(request.form['password'])
		)
		user.set_password(str(request.form['password']))
		user.save()
		return jsonify(user.to_hash())
	except:
		import sys
		print("Unexpected error:", sys.exc_info())

		return jsonify({'code' : 10001, 'msg' : "State already exists""}), 409


@app.route('/users/<user_id>', methods=['GET'])
def list_user_by_id(user_id):
	"""
	Get user by id
	list of the given user using user_id in databse
	---
	tags:
		- user
	parameters:
		-
			name: user_id
			in: path
			type: integer
			required: True
			description: user id
	responses:
		200:
			description: the User representation
			schema:
				$ref: '#/definitions/User'
		404:
			descripton: aboarts route, can not list user by id
	"""
	try:
		user = User.get(User.id == user_id)
		return jsonify(user.to_hash())
	except:
		abort(404)

@app.route('/users/<user_id>', methods=['PUT'])
def update_user_by_id(user_id):
	"""
	Update user
	Updates existing user and appends to database
	---
	tags:
		- user
	parameters:
		-
			name: user_id
			in: path
			type: integer
			required: True
			description: user id
	responses:
		409:
			descripton: notify that the email can not be changed
		200:
			description: the User representation
			schema:
				$ref: '#/definitions/User'
		404:
			descripton: user was not updated, error occured
	"""
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
		return jsonify(user.to_hash()), 200
	except:
		abort(404)


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
	"""
	Delete user
	Removes user specified by id from database
	---
	tags:
		- user
	parameters:
		-
			name: user_id
			in: path
			type: integer
			required: True
			description: user id
	responses:
		200:
			descripton: sucessfully deletes user
		404:
			descripton: user was not delted from database
	"""
	try:
		user = User.get(User.id == user_id)
		user.delete_instance()
		return jsonify({'msg' : 'success'}), 200
	except:
		abort(404)
