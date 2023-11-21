# #C:\flask_dev\flaskreact\models.py
# from flask_sqlalchemy import SQLAlchemy,Column, Integer
# from uuid import uuid4

 
# db = SQLAlchemy()
 
# def get_uuid():
#     return uuid4().hex
 
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.String(11), primary_key=True, unique=True, default=get_uuid)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.Text, nullable=False)
#     __tablename__ = "message"
#     id = db.Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(150))
#     message = db.Column (db.String(450))

#     __tablename__ = "loctions"
#     id = db.Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     radius = Column(Float, nullable=False, default=1.0)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Text, Float, Integer, ForeignKey
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(String(11), primary_key=True, unique=True, default=get_uuid)
    email = db.Column(String(150), unique=True)
    password = db.Column(Text, nullable=False)

class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(String(100))
    email = db.Column(String(150))
    message = db.Column(String(450))

class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(Integer, primary_key=True, unique=True, autoincrement=True)
    radius = Column(Float, nullable=False, default=1.0)
