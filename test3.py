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
user = User(name="Farouk", last_name="Ajmi",
        passwd="123456", birth="26-04-2000",
        email="farouk@handsome.com", type="ok", pic="../images/user_1.jpg", status="student", gender="Male")
user.save()

# Creation of a Post

post = Post(content="Where's my weed ?",
       sub_id="e0eb4841-6e87-4009-90ab-01028aa0fabd", u_id=user.id, cat_id="bdff7116-08ce-47ca-b317-2c166a1916e6")
post.save()

# Creation of a Comment
comment = Comments(content="Tequilaaaa", user_id="3c05d27c-1a53-4107-a708-e23d28b32b24", post_id=post.id)
comment.save()

models.storage.save()
