#!/usr/bin/python3
"""
Class Calendar
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Calendar(BaseModel, Base):
    """
    Representation of a calendar
    """
    __tablename__ = 'Calendar'
    c_date = Column(Date, nullable=False)
    text = Column(String(255), nullable=True)
    user_id = Column(String(60), ForeignKey('Users.id'), nullable=False)
    quest_id = Column(String(60), ForeignKey('Question.id'), nullable=False)
    ans_id = Column(String(60), ForeignKey('Answer.id'), nullable=False)
    act_id = Column(String(60), ForeignKey('Activity.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
