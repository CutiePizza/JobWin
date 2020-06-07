#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
import models
from models.user import User
from models.category import Category
from models.subcategory import Subcategory

# creation of a State
user = User(name="Sonya", last_name="CHokri",
        passwd="123456", birth="11-10-1998",
        email="sonya@joli.com", type="ok", pic=None, status="student", gender="female")
user.save()
cat = Category(name="Artificial intelligence")
cat.save()
sub = Subcategory(name="Machine learning", sub_id=cat.id)
sub.save()
models.storage.save()
print(user)
