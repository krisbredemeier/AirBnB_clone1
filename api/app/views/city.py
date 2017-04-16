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
			description: the City representation
			schema:
				$ref: '#/definitions/City'
		404:
			descripton: aboarts route, can not list user by id
	"""
	try:
		user = City.get(State.id == state_id)
		return jsonify(city.to_hash())
	except:
		abort(404)

@app.route('/states/<state_id>/cities', methods=['POST'])
def create_city():
    """
    Create a new city
    Creates a new city and appends to database
    ---
    tags:
        - city
    parameters:
        -
            name: city_name
            in: form
            type: string
            required: True
            description: the name of the state

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
                    city_name:
                        type: string
                        description: name of the city
                        required: true
        409:
            description: email already exists
    """
	try:
		city = City(
			city_name=str(request.form['name']),
		)
		city.save()
		return jsonify(city.to_hash())
	except:
		import sys
		print("Unexpected error:", sys.exc_info())

		return jsonify({'code' : 10002, 'msg' : "City already exists in this state"}), 409

@app.route('/states/<state_id>/cities/<city_id>', methods=['GET'])
def get_city_by_id(city_id):
	"""
	Get city by using state id
	list of the given state using state_id in databse
	---
	tags:
		- city
	parameters:
		-
			name: city_id
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
			descripton: aboarts route, can not list user by id
	"""
	try:
		city = City.get(city.id == city_id)
		return jsonify(city.to_hash())
	except:
		abort(404)


@app.route('/states/<state_id>/cities', methods=['PUT'])
def update_city_by_id(state_id):
	"""
	Update city
	Updates existing city and appends to database
	---
	tags:
		- state
	parameters:
		-
			name: city_id
			in: path
			type: integer
			required: True
			description: city id
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
		city = City.get(City.id == city_id)
		for key in request.values:
			if key == 'name':
				return jsonify({'msg' : 'City is already taken'}), 409
			if key == 'updated_at' or key == 'created_at':
				 continue
			else:
				 setattr(state, key, request.values.get(key))
		city.save()
		return jsonify(city.to_hash()), 200
	except:
		abort(404)


@app.route('/states/<state_id>/cities', methods=['DELETE'])
def delete_city_by_id(state_id):
	"""
	Delete city
	Removes city specified by id from database
	---
	tags:
		- city
	parameters:
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
			descripton: state was not delted from database
	"""
	try:
		city = City.get(City.id == city_id)
		city.delete_instance()
		return jsonify({'msg' : 'success'}), 200
	except:
		abort(404)
