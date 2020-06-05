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
    post_id = Column(Integer, primary_key=True)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=True)
    content = Column(String(255), nullable=True)
    sub_id = Column(Integer, ForeignKey('Subcategory.sub_id'), nullable=False)
    u_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    cat_id = Column(Integer, ForeignKey('Category.cat_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
