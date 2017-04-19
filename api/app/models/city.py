import peewee
from app.models.base import BaseModel
from app.models.state import State


class City(BaseModel):
    name = peewee.CharField(128, null=False)
    state = peewee.ForeignKeyField(State, related_name='cities', on_delete = "CASCADE")

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
            "name": self.name,
            "state_id": self.state.id,
        }
