
from app import app
from flask import render_template
from .services import *

@app.route('/')
def home():
    r_m = showChars()
    r_m.build_base()
    return render_template('index.html', r_m = r_m)

@app.route('/morty')
def morty():
    return render_template('morty.html')

@app.route('/rick')
def rick():
    return render_template('rick.html')

@app.route('/rando')
def rando():
    return render_template('rando.html')