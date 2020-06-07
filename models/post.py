#!/usr/bin/python3
"""
Class Post
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Post(BaseModel, Base):
    """
    Representation of a Post
    """
    __tablename__ = 'Post'
    content = Column(String(255), nullable=True)
    sub_id = Column(String(60), ForeignKey('Subcategory.id'), nullable=False)
    u_id = Column(String(60), ForeignKey('Users.id'), nullable=False)
    cat_id = Column(String(60), ForeignKey('Category.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
