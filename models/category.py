#!/usr/bin/python3
"""
Class category
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Answer(BaseModel, Base):
    """
    Representation of an Answer
    """
    __tablename__ = 'Category'
    cat_id = Column(Integer, primary_key=True)
    name= Column(String(255), nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
