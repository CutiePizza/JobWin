#!/usr/bin/python3
"""
Class Interview
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Interview(BaseModel, Base):
    """
    Representation of an Interview
    """
    __tablename__ = 'Interview'
    int_id = Column(Integer, primary_key=True)
    status = Column(String(255), nullable=False)
    submit_date = Column(Date, nullable=True)
    typee = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    cat_id = Column(Integer, ForeignKey('Category.cat_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
