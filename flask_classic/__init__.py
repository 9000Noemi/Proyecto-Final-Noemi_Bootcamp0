from flask import Flask, request, url_for

app = Flask(__name__, instance_relative_config=True)

app.config.from_object("config") 

ORIGIN_DATA = 'data/Movimientos.sqlite'

from flask_classic.routes import *

