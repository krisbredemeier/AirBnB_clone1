from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State
from app.models.place import Place
from app.models.city import City
from app.models.place_book import PlaceBook


@app.route('/places/<place_id>/books', methods=['GET'])
def get_book_by_id(place_id):
	"""
	Get book by place id
	list of the given book using place_id in databse
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
			description: the PlaceBook representation
			schema:
				$ref: '#/definitions/PlaceBook'
		404:
			descripton: aboarts route, can not list book by place id
	"""
	try:
		Place_book = PlaceBook.get(Place_book.id == place_book_id)
		return jsonify(place_book.to_hash())
	except:
		abort(404)

 @app.route('/places/<place_id>/books', methods=['POST'])
def creat_book():
"""
Create a new book
Creates a new book and appends to database
---
tags:
    - book
parameters:
    -
        name: book_name
        in: form
        type: string
        required: True
        description: the name of the book

responses:
    200:
        description: the Book representation
        schema:
            id: Book
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
                book_name:
                    type: string
                    description: name of the book
                    required: true
    409:
        description: book already exists
"""
try:
    book = PlaceBook
        book_name=str(request.form['name']),
    )
    book.save()
    return jsonify(book.to_hash())
except:
    import sys
    print("Unexpected error:", sys.exc_info())

    return jsonify({'code' : 10000, 'msg' : "Book name already exhists"}), 409

@app.route('/places/<place_id>/books/<book_id', methods=['GET'])
def list_book_by_id(book_id):
    """
    Get book by book id
    list of the given book using book_id in databse
    ---
    tags:
        - place_book
    parameters:
        -
            name: book_id
            in: path
            type: integer
            required: True
            description: book id
    responses:
        200:
            description: the PlaceBook representation
            schema:
                $ref: '#/definitions/PlaceBook'
        404:
            descripton: aboarts route, can not list book by id
    """
    try:
        book = PlaceBook.get(PlaceBook.id == book_id)
        return jsonify(book.to_hash())
    except:
        abort(404)

 @app.route('/places/<place_id>/books/<book_id>', methods=['PUTS'])
def update_book_by_id(place_id):
    """
    Update book
    Updates existing book and appends to database
    ---
    tags:
        - book
    parameters:
        -
            name: book_id
            in: path
            type: integer
            required: True
            description: book id
    responses:
        409:
            descripton: notify that user can't be changed
        200:
            description: the PlaceBook representation
            schema:
                $ref: '#/definitions/PlaceBook'
        404:
            descripton: book was not updated, error occured
    """
    try:
        book = PlaceBook.get(PlaceBook.id == book_id)
        for key in request.values:
            if key == 'user':
                return jsonify({'msg' : 'Book can not be changed'}), 409
            if key == 'updated_at' or key == 'created_at':
                 continue
            else:
                 setattr(book, key, request.values.get(key))
        book.save()
        return jsonify(book.to_hash()), 200
    except:
        abort(404)

@app.route('/places/<place_id>/books/<book_id>', methods=['DELETE'])
def delete_book_by_id(book_id):
	"""
	Delete book
	Removes book specified by id from database
	---
	tags:
		- book
	parameters:
		-
			name: book_id
			in: path
			type: integer
			required: True
			description: book id
	responses:
		200:
			descripton: sucessfully deletes book
		404:
			descripton: book was not delted from database
	"""
	try:
		book = PlaceBook.get(PlaceBook.id == book_id)
		book.delete_instance()
		return jsonify({'msg' : 'success'}), 200
	except:
		abort(404)
