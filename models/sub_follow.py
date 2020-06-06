#!/usr/bin/python3
"""
Class sub_follow
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Sub_follow(BaseModel, Base):
    """
    class Sub_follow
    """
    __tablename__ = 'Sub_follow'
    user1_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    user2_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    dat = Column(Date, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
