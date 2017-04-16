from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State
from app.model.city import City

/states/<state_id>/cities

@app.route('/states/<state_id>/cities', methods=['GET'])
def list_city_by_state(state_id):
	"""
	List city by state_id
	list of the given city using state_id in databse
	---
	tags:
		- city
	parameters:
		-
			name: state_id
			in: path
			type: integer
			required: True
			description: state id
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
