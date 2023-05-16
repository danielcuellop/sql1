import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    mail = Column(String(100))
    password = Column(String(20))
    favoritos = relationship("Favoritos", back_populates="usuario")

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", back_populates="address")

class Planetas(Base):
    __tablename__ = "planetas"
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(100))
    planet_population = Column(Integer)
    planet_cost = Column(Integer)
    planet_lenguage =Column(String(100))
    planet_king = Column(String(100))
    favoritos = relationship("Favoritos", back_populates="planetas")

class Personajes (Base):
    __tablename__ = "personajes"
    id = Column(Integer, primary_key=True)
    personaje_name = Column(String(100))
    personaje_age = Column(Integer)
    personaje_type = Column(String(100))
    personaje_movie = Column(String(100))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    favoritos = relationship("Favoritos", back_populates="personajes")

class Favoritos (Base):
    __tablename__ = "favoritos"
    id_favoritos = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", back_populates="favoritos")
    personaje_id = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship("Personajes", back_populates="favoritos")
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship("Planetas", back_populates="favoritos")

def to_dict(self):
    return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
