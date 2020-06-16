#!/usr/bin/python3
"""
Class Comments
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Comments(BaseModel, Base):
    """
    Representation of a Comment
    """
    __tablename__ = 'Comments'
    content = Column(String(500), nullable=False)
    user_id = Column(String(60), ForeignKey('Users.id'), nullable=False)
    post_id = Column(String(60), ForeignKey('Post.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
