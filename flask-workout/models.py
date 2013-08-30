'''
Created on Aug 30, 2013

@author: davide
'''
from sqlalchemy import Integer, String, Float
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class ExpenseContext(Base):
    """Main expenses contexts
    (Car, House, Medical etc.)
    """
    __tablename__ = 'contexts'
    
    id = Column(Integer, primary_key=True, sqlite_autoincrement=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

class Category(Base):
    """Categories of products inside a context
    (i.e. House maintenance) 
    """
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    context_id = Column(Integer, ForeignKey('contexts.id'))
    context = relationship('Context', backref=backref('contexts'))

    def __init__(self, name, context):
        self.name = name
        self.context_id = context
    
class Product(Base):
    """A simple element that has been bought
    (i.e. pelati Cirio 0.5)
    """
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand = Column(String)
    kilo_weight = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', backref=backref('categories'))

    def __init__(self, name, category):
        self.name = name
        self.category_id = category




    

#class Purchase(Base):
#    """
#    id
#    creation_date
#    customer
#    receipt_id
#    store_id
#    amount
#    """
#    pass
#
#class ProductsForPurchase(Base):
#    """
#    purchase_id
#    product_id
#    price
#    sale
#    """
#    pass
#
#class Store(Base):
#    """
#    id
#    name
#    address
#    """
#    
#class Document(Base):
#    """
#    id
#    description
#    filepath
#    creationdate
#    """
#    pass