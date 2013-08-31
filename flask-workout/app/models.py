'''
Created on Aug 30, 2013

@author: davide
'''
from database import Base
from sqlalchemy.schema import Column, Sequence, ForeignKey
from sqlalchemy.types import Integer, String, Float, Date
from sqlalchemy.orm import backref, relationship

class ExpenseContext(Base):
    """Main expenses contexts
    (Car, House, Medical etc.)
    """
    __tablename__ = 'contexts'
    
    id = Column(Integer, Sequence('context_id_seq'), primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return (self.name)
    
class Category(Base):
    """Categories of products inside a context
    (i.e. House maintenance) 
    """
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    context_id = Column(Integer, ForeignKey('contexts.id'))
    context = relationship('ExpenseContext', backref=backref('contexts'))

    def __init__(self, name, context):
        self.name = name
        self.context_id = context

    def __unicode__(self):
        return (self.name)
    
class Product(Base):
    """A simple element that has been bought
    (i.e. pelati Cirio 0.5)
    """
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand = Column(String)
    kilo_weight = Column(Float)
    expire_date = Column(Date)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', backref=backref('categories'))

    def __init__(self, name, brand, kilo_weight, expire_date, category):
        self.name = name
        self.brand = brand
        self.kilo_weight = kilo_weight
        self.expire_date = expire_date
        self.category_id = category

    def __unicode__(self):
        return (self.name)




    

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