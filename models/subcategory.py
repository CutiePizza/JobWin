#!/usr/bin/python3
"""
Class subcategory
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Varbinary
from sqlalchemy.orm import relationship


class Subcategory(BaseModel, Base):
    """
    class Subcategory
    """
    __tablename__ = 'Subcategory'
    sub_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    cat_id = Column(Integer, ForeignKey('Category.int_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
