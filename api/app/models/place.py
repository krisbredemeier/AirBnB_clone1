import peewee
from app.models.base import BaseModel
from app.models.user import User
from app.models.city import City


class Place(BaseModel):
    owner = peewee.ForeignKeyField(User, related_name = "places")
    city = peewee.ForeignKeyField(City, related_name = "places")
    name = peewee.CharField(128, null=False)
    description = peewee.TextField()
    number_rooms = peewee.IntegerField(default = 0)
    number_bathrooms = peewee.IntegerField(default = 0)
    max_guest = peewee.IntegerField(default = 0)
    price_by_night = peewee.IntegerField(default = 0)
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()


    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(args, kwargs)
        if kwargs is not None:	
            for k, v in kwargs.items():
                setattr(self, k, v)
        
    def to_hash(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "owner_id": self.owner.id,
            "city_id": self.city.id,
            "name": self.name,
            "description": self.description,
            "number_rooms": self.number_rooms,
            "number_bathrooms": self.number_bathrooms,
            "max_guest": self.max_guest,
            "price_by_night": self.price_by_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
