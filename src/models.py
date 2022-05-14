import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)

    def to_dict(self):
        return {}

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250),nullable=False)
    eye_color = Column(String(250),nullable=False)
    birth_year = Column(String(250),nullable=False)
    gender = Column(String(250),nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    homeworld = relationship('Planet')
    vehicles_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicles = relationship('Vehicles')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbiatal_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250),nullable=False)
    residents_id = Column(Integer, ForeignKey('people.id'))
    residents = relationship ('People')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    lenght = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    pilots_id = Column(Integer, ForeignKey('people.id'))
    pilots = relationship ('People')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planet.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    user = relationship('User')
    planet = relationship('Planet')
    people = relationship('People')
    

## Draw from SQLAlchemy base

# Here will start the instagram diagram as the repo for the instagram diagram exercise is not working properly

class UserInstagram(Base):
    __tablename__ = 'userInstagram'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Post (Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    poster_id = Column(Integer, ForeignKey('userInstagram.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('userInstagram.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media (Base):
    __tablename__ = 'media'
    id = Column (Integer, primary_key=True)
    type = Column (String(250), nullable=False)
    url = Column (String(250), nullable=False)
    post_id = Column (Integer, ForeignKey('post.id'))

class Follower (Base):
    __tablename__ = 'follower'
    id = Column (Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('userInstagram.id'))
    user_to_id = Column(Integer, ForeignKey('userInstagram.id'))

render_er(Base, 'diagram.png')