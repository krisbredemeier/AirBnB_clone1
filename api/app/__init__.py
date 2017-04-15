from flask import Flask
from flask_json import FlaskJSON
from config import *
from flasgger import Swagger

# __all__ = ["config"]

app = Flask(__name__)
FlaskJSON(app)

from views import *
