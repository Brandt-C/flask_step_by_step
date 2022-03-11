from flask import Flask

from config import Config

app = Flask(__name__, static_url_path='/static', static_folder='static')

app.config.from_object(Config)

from . import routes