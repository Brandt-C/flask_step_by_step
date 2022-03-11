
from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/morty')
def morty():
    return render_template('morty.html')

@app.route('/rick')
def rick():
    return render_template('rick.html')

@app.route('/rando')
def rando():
    return render_template('rando.html')