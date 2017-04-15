import peewee
import md5
from app.models.base import BaseModel
# database = peewee.SqliteDatabase("database",  pragmas=(('foreign_keys', True), ))


class User (BaseModel):
    email = peewee.CharField(128, null=False, unique=True)
    password = peewee.CharField(128, null=False)
    first_name = peewee.CharField(128, null=False)
    last_name = peewee.CharField(128, null=False)
    is_admin = peewee.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__()

    def set_password(self, clear_password):
        self.pasword = md5.new(clear_password).hexidigest()

    def to_hash(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin
        }
