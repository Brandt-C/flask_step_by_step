

import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    """
    set config variable for our entire flask app
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')