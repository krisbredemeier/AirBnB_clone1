import peewee
from app.models.base import BaseModel

class State(BaseModel):
    name = peewee.CharField(128, null = False, unique = True)


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
        }
