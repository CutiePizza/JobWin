#!/usr/bin/python3
"""
Class Post_like
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Post_like(BaseModel, Base):
    """
    class Post_like
    """
    __tablename__ = 'Post_like'
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.post_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
