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
        super(BaseModel, self).__init__()
        
    def to_hash(self):
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "owner_id": User.id,
            "city_id": City.id,
            "name": self.__name,
            "description": self.__description,
            "number_rooms": self.__number_rooms,
            "number_bathrooms": self.__number_bathrooms,
            "max_guest": self.__max_guest,
            "price_by_night": self.__price_by_night,
            "latitude": self.__latitude,
            "longitude": self.__longitude,
        }
