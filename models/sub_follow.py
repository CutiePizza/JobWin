#!/usr/bin/python3
"""
Class sub_follow
"""
import models
from models.second_base_model import SecondBaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Sub_follow(SecondBaseModel, Base):
    """
    class Sub_follow
    """
    __tablename__ = 'Sub_follow'
    id_1 = Column(String(60), ForeignKey('Users.id'), primary_key=True)
    id_2 = Column(String(60), ForeignKey('Users.id'), primary_key=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
