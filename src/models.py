import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    user_name = Column(String(250),unique=True)
    email=Column(String(250),unique=True)
    password=Column(String(100))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter=Column(Integer)
    rotation_period=Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(60))
    population = Column(Integer)
    climate = Column(String(60))
    terrain = Column(String(60))
    surface_water = Column(String(60))
    created = Column(DateTime)
    edited = Column(DateTime)
    name = Column(String(60))
    url = Column(String(200))
    description = Column(String(550))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(String(60), primary_key=True)
    height=Column(Integer)
    mass=Column(Integer)
    hair_color = Column(String(60))
    skin_color = Column(String(60))
    eye_color = Column(String(60))
    birth_year=Column(Date)
    gender = Column(String(60))
    created = Column(DateTime)
    created = Column(DateTime)
    name = Column(String(60))
    homewold = Column(String(200))
    url = Column(String(200))
    description = Column(String(550))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')