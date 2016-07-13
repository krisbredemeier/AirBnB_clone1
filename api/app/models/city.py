import peewee
import state

@app.route()
class City(BaseModel):
    name = peewee.CharField(128, null=False)
    state = peewee.ForeignKeyField(state, related-name= 'cities', on_delete = "CASCADE")
