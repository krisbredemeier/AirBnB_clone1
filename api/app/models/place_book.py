import peewee
from app.models.base import BaseModel
from app.models.place import Place
from app.models.user import User


class PlaceBook(BaseModel):
    place = peewee.ForeignKeyField(Place)
    user = peewee.ForeignKeyField(User, related_name = "placesbooked")
    is_validated = peewee.BooleanField(default=False)
    date_start = peewee.DateTimeField(null = False)
    number_nights = peewee.IntegerField(default = 1)

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
            "place_id": self.place.id,
            "user_id": self.user.id,
            "is_validated": self.is_validated,
            "date_start": self.date_start,
            "number_nights": self.number_nights,
        }
