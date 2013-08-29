from sqlalchemy import create_engine, Integer, String
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship, backref

db = create_engine('sqlite:///workout.db', echo=True)

Base = declarative_base()

class Film(Base):
    
    __tablename__ = 'films'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    director_id = Column(Integer, ForeignKey('directors.id'))
    director = relationship('Director', backref=backref('films', order_by='id'))

    def __init__(self, name):
        self.name = name
        
class Director(Base):
    
    __tablename__ = 'directors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name
        
Base.metadata.create_all(db)