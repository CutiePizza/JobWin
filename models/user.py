#!/usr/bin/python3
"""
Class Users
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Representation of a User
    """
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    passwd = Column(String(255), nullable=False)
    birth = Column(String(255), nullable=True)
    email = Column(String(255), nullable=False)
    typee = Column(String(255), nullable=False)
    pic = Column(Varbinary(5000), nullable=True)
    status = Column(String(255), nullable=True)
    gender = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
