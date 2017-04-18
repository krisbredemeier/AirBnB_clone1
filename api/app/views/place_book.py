from flask import Flask, jsonify, request, abort
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State
from app.models.place import Place
from app.models.city import City
from app.models.place_book import PlaceBook

from datetime import datetime

@app.route('/places/<place_id>/books', methods=['GET'])
def get_books_by_id(place_id):
	"""
	Get book by place id
	list of the given book using place_id in databse
	---
	tags:
		- book
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
		place_books = []
		for place_book in PlaceBook.select().join(Place).where(Place.id == place_id):
			place_books.append(place_book.to_hash())
		return jsonify(place_books), 200
	except:
		abort(404)

@app.route('/places/<place_id>/books', methods=['POST'])
def create_book(place_id):
	"""
	Create a new book
	Creates a new book and appends to database
	---
	tags:
		- book
	parameters:
		-
			name: place_id
			in: path
			type: integer
			required: True
			description: place id
		-
			name: date_start
			in: form
			type: date-time
			required: True
			description: the date of booking
		-
			name: user_id
			in: form
			type: integer
			required: True
			description: User id
		-
			name: number_nights
			in: form
			type: integer
			required: False
			description: Number of nights
		-
			name: is_validated
			in: form
			type: boolean
			required: False
			description: book validated

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
					date_start:
						type: date-time
						description: the date of booking
						required: true
					number_nights:
						type: number
						description: Number of nights
					is_validated:
						type: boolean
						description: book validated
		409:
			description: book already exists
	"""
	try:
		b_is_validated = False
		if request.form.get('is_validated') == 1 or request.form.get('is_validated') == "true":
			b_is_validated = True
		d_date_start = None
		s_date_start = request.form.get('date_start')
		if s_date_start is not None:
			d_date_start = datetime.strptime(s_date_start, '%Y/%m/%d %H:%M:%S') 
		book = PlaceBook(
			place_id=Place.get(Place.id == place_id),
			user_id=User.get(User.id==request.form.get('user_id')),
			date_start=d_date_start,
			number_nights=request.form.get('number_nights', 1),
			is_validated=b_is_validated
		)
		book.save()
		return jsonify(book.to_hash())
	except:
		import sys
		print("Unexpected error:", sys.exc_info())

		return jsonify({'code' : 10000, 'msg' : "Book name already exhists"}), 409

@app.route('/places/<place_id>/books/<book_id>', methods=['GET'])
def list_book_by_id(place_id, book_id):
	"""
	Get book by book id
	list of the given book using book_id in databse
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
			description: the PlaceBook representation
			schema:
				$ref: '#/definitions/PlaceBook'
		404:
			descripton: aboarts route, can not list book by id
	"""
	try:
		book = PlaceBook.select().join(Place).where(Place.id == place_id).where(PlaceBook.id == book_id).get()
		return jsonify(book.to_hash())
	except:
		abort(404)

@app.route('/places/<place_id>/books/<book_id>', methods=['PUT'])
def update_book_by_id(place_id, book_id):
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
		book = PlaceBook.select().join(Place).where(Place.id == place_id).where(PlaceBook.id == book_id).get()
		for key in request.values:
			if key == 'user_id':
				return jsonify({'msg' : 'user can not be changed'}), 409
			if key == 'updated_at' or key == 'created_at':
				 continue
			else:
				 setattr(book, key, request.values.get(key))
		book.save()
		return jsonify(book.to_hash()), 200
	except:
		abort(404)

@app.route('/places/<place_id>/books/<book_id>', methods=['DELETE'])
def delete_book_by_id(place_id, book_id):
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
		book = PlaceBook.select().join(Place).where(Place.id == place_id).where(PlaceBook.id == book_id).get()
		book.delete_instance()
		return jsonify({'msg' : 'success'}), 200
	except:
		abort(404)
