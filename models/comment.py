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
    com_id = Column(Integer, primary_key=True)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=True)
    content = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.post_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
