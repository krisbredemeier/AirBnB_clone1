import peewee
from app.models.base import BaseModel
from app.models.state import State


class City(BaseModel):
    name = peewee.CharField(128, null=False)
    state = peewee.ForeignKeyField(State, related_name='cities', on_delete = "CASCADE")

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__()
        
    def to_hash(self):
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "name": self.__name,
            "state_id": State.id,
        }
