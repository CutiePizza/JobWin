#!/usr/bin/python3
"""
Class Correction
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Correction(BaseModel, Base):
    """
    Representation of a Correction
    """
    __tablename__ = 'Correction'
    c_date = Column(Date, nullable=False)
    text = Column(String(255), nullable=True)
    feedback = Column(String(255), nullable=True)
    int_id = Column(String(60), ForeignKey('Interview.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('Users.id'), nullable=False)
    coach_id = Column(String(60), ForeignKey('User.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
