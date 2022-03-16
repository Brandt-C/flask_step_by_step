from flask import Flask

from config import Config

from .user.routes import user 


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(user)


from . import routes