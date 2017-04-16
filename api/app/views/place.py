from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State



@app.route('/places', methods=['GET'])
def list_places():
	"""
	Get all places
	This will list all places in the database
	---
	tags:
		- places
	responses:
		200:
			description: return list of all places
			schema:
				type: array
				items:
					$ref: '#/definitions/Place'
	"""
	places = []
	for place in Place.select():
		places.append(place.to_hash())
	return jsonify(places), 200

@app.route('/places/<place_id>', methods=['GET'])
def get_place_by_id(place_id):
	"""
	Get place by id
	list of the given places using place_id in databse
	---
	tags:
		- place
	parameters:
		-
			name: place_id
			in: path
			type: integer
			required: True
			description: place id
	responses:
		200:
			description: the Place representation
			schema:
				$ref: '#/definitions/Place'
		404:
			descripton: aboarts route, can not list user by id
	"""
	try:
		place = Place.get(Place.id == place_id)
		return jsonify(place.to_hash())
	except:
		abort(404)
