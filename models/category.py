#!/usr/bin/python3
"""
Class category
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """
    category class
    """
    __tablename__ = 'Category'
    name= Column(String(255), nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
