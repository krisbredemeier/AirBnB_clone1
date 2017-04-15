import peewee
# hacky way of importing models
from app.models import mysql_database
from app.models.amenity import *
from app.models.base import *
from app.models.city import *
from app.models.place_amenity import *
from app.models.place_book import *
from app.models.place import *
from app.models.state import *
from app.models.user import *

models = {
	'amenity': Amenity,
	'base': BaseModel,
	'city': City,
	'place_amenity': PlaceAmenity,
	'place_book': PlaceBook,
	'place': Place,
	'state': State,
	'user': User
}

mysql_database.connect()
mysql_database.create_tables([
	Amenity,
	City,
	PlaceAmenity,
	PlaceBook,
	Place,
	State,
	User
])
