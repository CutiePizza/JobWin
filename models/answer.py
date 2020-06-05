#!/usr/bin/python3
"""
Class Answer
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Varbinary
from sqlalchemy.orm import relationship


class Answer(BaseModel, Base):
    """
    Representation of an Answer
    """
    __tablename__ = 'Answer'
    a_id = Column(Integer, primary_key=True)
    text = Column(String(255), nullable=True)
    audio = Column(Varbinary(5000), nullable=True)
    int_id = Column(Integer, ForeignKey('Interview.int_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
