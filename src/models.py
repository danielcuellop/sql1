import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    mail = Column(String(100))
    password = Column(String(20))
    


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)

class Planetas(Base):
    __tablename__ = "planetas"
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(100))
    planet_population = Column(Integer)
    planet_cost = Column(Integer)
    planet_lenguage =Column(String(100))
    planet_king = Column(String(100))

class Personaje (Base):
    __tablename__ = "personaje"
    id = Column(Integer, primary_key=True)
    personaje_name = Column(String(100))
    personaje_age = Column(Integer)
    personaje_type = Column(String(100))
    personaje_movie = Column(String(100))
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
