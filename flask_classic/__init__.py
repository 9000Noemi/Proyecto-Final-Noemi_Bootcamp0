from flask import Flask

app = Flask(__name__)

app.config.from_object("secret")

ORIGIN_DATA = 'data/Movimientos.sqlite'

from flask_classic.routes import *

