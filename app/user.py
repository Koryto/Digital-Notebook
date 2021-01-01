from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from .database import db

base = declarative_base()
base.metadata.create_all(bind=db)

class User(base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    # Define Table Schema
    id = Column(Integer, primary_key=True)
    email = Column(String)
    city = Column(String)

    def __init__(self, email, city):
        self.email = email
        self.city = city

    def __repr__(self):
        return f'<User id {self.id}>'

    def serialize(self):
        return  {
            'id': self.id,
            'email': self.email,
            'city': self.city,
        }

