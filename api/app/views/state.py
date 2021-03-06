from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State

@app.route('/states', methods=['GET'])
def list_states():
	"""
	Get all states
	This will list all states in the database
	---
	tags:
		- state
	responses:
		200:
			description: return list of all states
			schema:
				type: array
				items:
					$ref: '#/definitions/State'
	"""
	states = []
	for state in State.select():
		states.append(state.to_hash())
	return jsonify(states), 200

@app.route('/states', methods=['POST'])
def create_state():
    """
    Create a new states
    Creates a new states and appends to database
    ---
    tags:
        - state
    parameters:
        -
            name: name
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
                    name:
                        type: string
                        description: name of the state
                        required: true
        409:
            description: email already exists
    """
    try:
        state = State(
            name=str(request.form['name']),
        )
        state.save()
        return jsonify(state.to_hash())
    except:
        import sys
        print("Unexpected error:", sys.exc_info())

        return jsonify({'code' : 10000, 'msg' : "State name already exhists"}), 409

@app.route('/states/<state_id>', methods=['GET'])
def get_state_by_id(state_id):
	"""
	Get state by id
	list of the given state using state_id in databse
	---
	tags:
		- state
	parameters:
		-
			name: state_id
			in: path
			type: integer
			required: True
			description: state id
	responses:
		200:
			description: the State representation
			schema:
				$ref: '#/definitions/State'
		404:
			descripton: aboarts route, can not list user by id
	"""
	try:
		state = State.get(State.id == state_id)
		return jsonify(state.to_hash())
	except:
		abort(404)


@app.route('/states/<state_id>', methods=['PUT'])
def update_state_by_id(state_id):
	"""
	Update state
	Updates existing state and appends to database
	---
	tags:
		- state
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
			description: the name of the state
	responses:
		200:
			descripton: the State representation
			schema:
				$ref: '#/definitions/State'
		404:
			descripton: state was not updated, error occured
		409:
			descripton: name is already taken in the database,
	"""
	try:
		state = State.get(State.id == state_id)
		for key in request.values:
			if key == 'updated_at' or key == 'created_at':
				 continue
			else:
				 setattr(state, key, request.values.get(key))
		state.save()
		return jsonify(state.to_hash()), 200
	except:
		abort(404)


@app.route('/states/<state_id>', methods=['DELETE'])
def delete_state_by_id(state_id):
	"""
	Delete state
	Removes state specified by id from database
	---
	tags:
		- state
	parameters:
		-
			name: state_id
			in: path
			type: integer
			required: True
			description: state id
	responses:
		200:
			descripton: sucessfully deletes state
		404:
			descripton: state was not delted from database
	"""
	try:
		state = State.get(State.id == state_id)
		state.delete_instance()
		return jsonify({'msg' : 'success'}), 200
	except:
		abort(404)
