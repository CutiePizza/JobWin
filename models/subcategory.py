#!/usr/bin/python3
"""
Class subcategory
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date, VARBINARY
from sqlalchemy.orm import relationship


class Subcategory(BaseModel, Base):
    """
    class Subcategory
    """
    __tablename__ = 'Subcategory'
    name = Column(String(255), nullable=True)
    cat_id = Column(String(60), ForeignKey('Category.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
