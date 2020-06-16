#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
import models
from models.user import User
from models.post import Post
from models.comment import Comments
from models.interview import Interview
from models.answer import Answer
from models.correction import Correction
from models.category import Category
from models.subcategory import Subcategory
from models.sub_follow import Sub_follow
from models.relation import Relation
from models.comm_like import Comm_like
from models.post_like import Post_like
from models.question import Question

# Creation of a user
user = User(name="Yasmine", last_name="Hamdi",
        passwd="123456", birth="12-11-1997",
        email="sonya@joli.com", type="ok", pic=None, status="student", gender="female")
user.save()

user2 = User(name="Salmen", last_name="Zouari",
        passwd="salmeeeenz", birth="unknown", email="sal@gmail.com",
        type="ok2", pic=None, status="Student", gender="Male")
user2.save()

# Creation of a category
cat = Category(name="Programming")
cat.save()

# Creation of a subcategory
sub = Subcategory(name="Python", sub_id=cat.id)
sub.save()

# Creation of an Interview
interview = Interview(status="Done", submit_date="2020-06-15", type="hakuna batata",
        user_id=user.id, cat_id=cat.id)
interview.save()

# Creation of a Post

post = Post(content="Hello guys! I would like to know how is the working environment in Sanatnder",
        sub_id=sub.id, user_id=user.id, cat_id=cat.id)
post.save()

# Creation of a Comment
comment = Comments(content="It is very friendly", user_id=user2.id, post_id=post.id)
comment.save()

# Creation of a question 
question = Question(text="Who created the Python programming language", type="Python",
        sub_id=sub.id, int_id=interview.id)
question.save()

# Creation of an Answer

ans = Answer(text="Guido Van rossum", audio=None, int_id=interview.id)
ans.save()

models.storage.save()
