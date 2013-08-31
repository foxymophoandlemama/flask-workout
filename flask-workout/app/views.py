'''
Created on Aug 29, 2013

@author: davide
'''
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

from database import db_session
from models import Product

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)