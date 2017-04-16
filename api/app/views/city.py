from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State

/states/<state_id>/cities

@app.route('/states/<state_id>/cities', methods=['GET'])
def list_city_by_state(state_id):
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
