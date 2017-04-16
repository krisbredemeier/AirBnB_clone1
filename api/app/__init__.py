from flask import Flask
from flask_json import FlaskJSON
from config import *
from flasgger import Swagger


app = Flask(__name__)

app.config['SWAGGER'] = {
    "swagger_version": "2.0"
}
Swagger(app)

FlaskJSON(app)




from app.views import *


