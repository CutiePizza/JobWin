#!/usr/bin/python3
"""
Class Question
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Question(BaseModel, Base):
    """
    Representation of a Question
    """
    __tablename__ = 'Question'
    q_id = Column(Integer, primary_key=True)
    text = Column(String(255), nullable=True)
    sub_id = Column(Integer, ForeignKey('Subcategory.sub_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
