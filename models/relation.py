#!/usr/bin/python3
"""
Class realtion
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Relation(BaseModel, Base):
    """
    class relation
    """
    __tablename__ = 'Relation'
    user_id = Column(Integer, primary_key=True)
    dat = Column(Date, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
