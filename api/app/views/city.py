from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State
from app.models.city import City


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
			description: the City representation
			schema:
				$ref: '#/definitions/City'
		404:
			descripton: aboarts route, can not list city by id
	"""
	try:
		cities = []
		for city in City.select().join(State).where(State.id == state_id):
			cities.append(city.to_hash())
		return jsonify(cities), 200
	except:
		abort(404)

@app.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
	"""
	Create a new city
	Creates a new city and appends to database
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
		-
			name: name
			in: form
			type: string
			required: True
			description: the name of the city

	responses:
		200:
			description: the City representation
			schema:
				id: City
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
					name:
						type: string
						description: name of the city
						required: true
		409:
			description: city already exists
	"""
	try:
		city = City(
			name=str(request.form['name']),
			state_id=State.get(State.id == state_id).id
		)
		city.save()
		return jsonify(city.to_hash())
	except:
		return jsonify({'code' : 10002, 'msg' : "City already exists in this state"}), 409

@app.route('/states/<state_id>/cities/<city_id>', methods=['GET'])
def get_city_by_id(state_id, city_id):
	"""
	Get city by using city id
	list of the given city using city_id in databse
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
		-
			name: city_id
			in: path
			type: integer
			required: True
			description: city id
	responses:
		200:
			description: the City representation
			schema:
				$ref: '#/definitions/City'
		404:
			descripton: aboarts route, can not list city by id
	"""
	try:
		city = City.select().join(State).where(State.id == state_id).where(City.id == city_id).get()
		return jsonify(city.to_hash())
	except:
		import sys
		print("Unexpected error:", sys.exc_info())
		abort(404)


@app.route('/states/<state_id>/cities/<city_id>', methods=['PUT'])
def update_city_by_id(state_id, city_id):
 	"""
	Update city
 	Updates existing city and appends to database
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
 		-
 			name: city_id
 			in: path
 			type: integer
 			required: True
 			description: city id
		-
			name: name
			in: form
			type: string
			required: True
			description: the name of the city
 	responses:
 		409:
 			descripton: name is already taken in the database,
 		200:
 			description: the City representation
 			schema:
 				$ref: '#/definitions/City'
 		404:
 			descripton: state was not updated, error occured
 	"""
 	try:
 		city = City.select().join(State).where(State.id == state_id).where(City.id == city_id).get()
 		for key in request.values:
 			if key == 'updated_at' or key == 'created_at':
 				 continue
 			else:
 				 setattr(city, key, request.values.get(key))
 		city.save()
 		return jsonify(city.to_hash()), 200
 	except:
 		abort(404)


@app.route('/states/<state_id>/cities/<city_id>', methods=['DELETE'])
def delete_city_by_id(state_id, city_id):
	"""
	Delete city
	Removes city specified by id from database
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
		-
			name: city_id
			in: path
			type: integer
			required: True
			description: city id
	responses:
		200:
			descripton: sucessfully deletes city
		404:
			descripton: city was not delted from database
	"""
	try:
		city = City.select().join(State).where(State.id == state_id).where(City.id == city_id).get()
		city.delete_instance()
		return jsonify({'msg' : 'success'}), 200
	except:
		abort(404)
