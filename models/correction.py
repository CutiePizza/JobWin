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
    c_id = Column(Integer, primary_key=True)
    c_date = Column(Date, nullable=False)
    text = Column(String(255), nullable=True)
    feedback = Column(String(255), nullable=True)
    int_id = Column(Integer, ForeignKey('Interview.int_id'), nullable=False)
    u_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    coach_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
