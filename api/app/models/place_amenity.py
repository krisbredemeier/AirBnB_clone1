import peewee
from app.models.base import BaseModel
from app.models.amenity import Amenity
from app.models.place import Place


class PlaceAmenity(peewee.Model):
    place = peewee.ForeignKeyField(Place)
    amenity = peewee.ForeignKeyField(Amenity)

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(args, kwargs)
        if kwargs is not None:	
            for k, v in kwargs.items():
                setattr(self, k, v)