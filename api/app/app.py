from flask import Flask
from app import app
from app.views import *
from config import HOST, PORT, DEBUG

if __name__ == '__main__':
    app.run(host=HOSt, port=PORT, debug=DEBUG)