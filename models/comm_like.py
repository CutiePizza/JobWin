#!/usr/bin/python3
"""
Class comm_like
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Comm_like(BaseModel, Base):
    """
    class Comm_like
    """
    __tablename__ = 'Comm_like'
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    com_id = Column(Integer, ForeignKey('Comments.com_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
