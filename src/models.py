import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    posts = relationship("Post", back_populates="user")
    followers = relationship("Followers", back_populates="user", cascade="all, delete-orphan")
    following = relationship("Followers", back_populates="follower", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="user")


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    caption = Column(String(200))
    image_url = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class Followers(Base):
    __tablename__ = 'followers'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    follower_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship("User", back_populates="following", foreign_keys=[user_id])
    follower = relationship("User", back_populates="followers", foreign_keys=[follower_id])


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="comments")
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Post", back_populates="comments")


def to_dict(self):
    return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
