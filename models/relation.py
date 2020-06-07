#!/usr/bin/python3
"""
Class realtion
"""
import models
from models.second_base_model import SecondBaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Relation(SecondBaseModel, Base):
    """
    class relation
    """
    __tablename__ = 'Relation'
    id_1 = Column(String(60), primary_key=True) # followed user
    id_2 = Column(String(60), primary_key=True) # followed by user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
