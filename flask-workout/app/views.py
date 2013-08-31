'''
Created on Aug 29, 2013

@author: davide
'''
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

from database import db_session
from models import Product, Category, ExpenseContext

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    contexts = ExpenseContext.query.all()
    return render_template('index.html', contexts=contexts)

@app.route('/get_categories_by_context')
def get_categories_by_context(context_id):
    categories = Category.query.filter(Category.context_id==context_id).all()
    return render_template('index.html', categories=categories)
    
    
    