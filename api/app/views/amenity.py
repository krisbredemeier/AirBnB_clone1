from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State
from app.models.place import Place
from app.models.city import City
from app.models.place_book import PlaceBook
from app.models.amenity import Amenity


@app.route('/amenities', methods=['GET'])
def list_amenities():
	"""
	Get all amenities
	This will list all amenities in the database
	---
	tags:
		- amenity
	responses:
		200:
			description: return list of all amenties
			schema:
				type: array
				items:
					$ref: '#/definitions/Amenity'
	"""
	amenity = []
	for amenity in Amenity.select():
		amenties.append(amenity.to_hash())
	return jsonify(amenites), 200

 @app.route('/amenities', methods=['POST'])
def creat_amenity():
"""
Create a new amenity
Creates a new amenity and appends to database
---
tags:
    - amenity
parameters:
    -
        name: amenity_name
        in: form
        type: string
        required: True
        description: the name of the amenity

responses:
    200:
        description: the Amenity representation
        schema:
            id: Amenity
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
                amenity_name:
                    type: string
                    description: name of the amenity
                    required: true
    409:
        description: amenity already exists
"""
try:
    amenity = amenity
        amenity_name=str(request.form['name']),
    )
    amenity.save()
    return jsonify(amentiy.to_hash())
except:
    import sys
    print("Unexpected error:", sys.exc_info())

    return jsonify({'code' : 10000, 'msg' : "Amenity name already exhists"}), 409

@app.route('/amenities/<amenity_id>', methods=['GET'])
def list_amenity_by_id(amenity_id):
    """
    Get amenity by amenity id
    list of the given book using amenity_id in databse
    ---
    tags:
        - amenity
    parameters:
        -
            name: amenity_id
            in: path
            type: integer
            required: True
            description: book id
    responses:
        200:
            description: the Amenity representation
            schema:
                $ref: '#/definitions/Amenity'
        404:
            descripton: aboarts route, can not list amenity by id
    """
    try:
        amenity = Amenity.get(Amenity.id == amentiy_id)
        return jsonify(amenity.to_hash())
    except:
        abort(404)

@app.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amentiy_by_id(amenity_id):
	"""
	Delete amenity
	Removes amenity specified by id from database
	---
	tags:
		- amentiy
	parameters:
		-
			name: amentiy_id
			in: path
			type: integer
			required: True
			description: amentiy id
	responses:
		200:
			descripton: sucessfully deletes amenity
		404:
			descripton: amenity was not delted from database
	"""
	try:
		amentiy = Amenity.get(Amenity.id == amentiy_id)
		amenity.delete_instance()
		return jsonify({'msg' : 'success'}), 200
	except:
		abort(404)

@app.route('/places/<place_id>/amenities', methods=['GET'])
def list_amenity_by_place(place_id):
	"""
	List amenity by place_id
	list of the given amenities using place_id in databse
	---
	tags:
		- amenity
	parameters:
		-
			name: place_id
			in: path
			type: integer
			required: True
			description: place id
	responses:
		200:
			description: the Amenity representation
			schema:
				$ref: '#/definitions/Amenity'
		404:
			descripton: aboarts route, can not list amenity by place id
	"""
	try:
		amenity = Amenity.get(Amenity.id == amenity_id)
		return jsonify(amenity.to_hash())
	except:
		abort(404)
