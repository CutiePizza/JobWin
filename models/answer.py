#!/usr/bin/python3
"""
Class Answer
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date, VARBINARY
from sqlalchemy.orm import relationship


class Answer(BaseModel, Base):
    """
    Representation of an Answer
    """
    __tablename__ = 'Answer'
    text = Column(String(255), nullable=True)
    audio = Column(VARBINARY(5000), nullable=True)
    int_id = Column(String(60), ForeignKey('Interview.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
