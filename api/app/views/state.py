from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State

@app.route('/states', methods=['GET'])
def list_states():
	states = []
	for state in State.select():
		state.append(state.to_hash())
	return jsonify(states), 200

@app.route('/states', methods=['POST'])
def create_state():
	try:
		state = State(
			first_name=str(request.form['first_name']),
			last_name=str(request.form['last_name']),
			email=str(request.form['email']),
			is_admin=False,
		)
		user.save()
		return jsonify(state.to_hash())
	except:
		import sys
		print("Unexpected error:", sys.exc_info())

		return jsonify({'code' : 10000, 'msg' : "Email already exists"}), 409
