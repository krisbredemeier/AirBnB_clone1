import peewee
from datetime import datetime
from config import *


'''
=======================
base python starts here
=======================
'''

class BaseModel(peewee.Model):
	"""docstring for BaseModel"""

	id = peewee.PrimaryKeyField(unique = True)
	updated_at = peewee.DateTimeField(default = datetime.now().strftime('%Y/%m/%d %H:%M;%S'))
	created_at = peewee.DateTimeField(default = datetime.now().strftime('%Y/%m/%d %H:%M;%S'))

	# init func
	def __init__(self, *args, **kwargs):
		pass

	# save func TODO more comments
	def save(self):
		self.update_at = datetime.now().strftime('%Y/%m/%d %H:%M;%S')
		peewee.Model.save(self)

	# metaclass func
	class Meta():
		from app.models import mysql_database
		database = mysql_database
		order_by = ("id", )
