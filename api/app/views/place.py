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

@app.route('/places', methods=['POST'])
def creat_place():

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

@app.route('/places/<place_id>', methods=['PUTS'])
def update_place_by_id(place_id):
"""
Update place
Updates existing place and appends to database
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
    409:
        descripton: notify that owner and city can't be changed
    200:
        description: the User representation
        schema:
            $ref: '#/definitions/User'
    404:
        descripton: user was not updated, error occured
"""
try:
    place = Place.get(Place.id == place_id)
    for key in request.values:
        if key == 'owner' or 'city':
            return jsonify({'msg' : 'owner and city can not be changed'}), 409
        if key == 'updated_at' or key == 'created_at':
             continue
        else:
             setattr(user, key, request.values.get(key))
    place.save()
    return jsonify(place.to_hash()), 200
except:
    abort(404)

@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place_by_id(state_id):
	"""
	Delete place
	Removes place specified by id from database
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
			descripton: sucessfully deletes place
		404:
			descripton: state was not delted from database
	"""
	try:
		place = Place.get(Place.id == place_id)
		place.delete_instance()
		return jsonify({'msg' : 'success'}), 200
	except:
		abort(404)

@app.route('/states/<state_id>/cities/<city_id>/places', methods=['GET'])
def list_place_by_city(city_id):


@app.route('/states/<state_id>/cities/<city_id>/places', methods=['POST'])
def creae_new_place(city_id):
