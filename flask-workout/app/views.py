'''
Created on Aug 29, 2013

@author: davide
'''
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

import models

@app.route('/')
def index():
    products = models.Product.query.all()
    return render_template('index.html', products=products)