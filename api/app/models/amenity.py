import peewee
from app.models.base import BaseModel

class Amenity(BaseModel):
    name = peewee.CharField(128, null=False)

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__()
        
    def to_hash(self):
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "name": self.__name,
        }
