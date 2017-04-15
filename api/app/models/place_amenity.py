import peewee
from app.models.base import BaseModel
from app.models.amenity import Amenity
from app.models.place import Place


class PlaceAmenity(peewee.Model):
    place = peewee.ForeignKeyField(Place)
    amenity = peewee.ForeignKeyField(Amenity)

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__()
