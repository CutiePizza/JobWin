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
user = User(name="Ines", last_name="Chokri",
        passwd="123456", birth="26-04-1997",
        email="ines.chokri@joli.com", type="ok", pic="../images/user_1.jpg", status="student", gender="female")
user.save()

user2 = User(name="Houssem", last_name="eddine ben khalifa",
        passwd="houss", birth="unknown", email="elmatador@gmail.com",
        type="ok2", pic="../images/user_2.jpg", status="Student", gender="Male")
user2.save()

# Creation of a category
at = Category(name="AI")
cat.save()

# Creation of a subcategory
sub = Subcategory(name="Machine learning", sub_id=cat.id)
sub.save()

# Creation of an Interview
interview = Interview(status="Done", submit_date="2020-06-15", type="hakuna batata", user_id=user.id, cat_id=cat.id)
interview.save()

# Creation of a Post

post = Post(content="Any good website for cheating ?",
        sub_id=sub.id, u_id=user2.id, cat_id=cat.id)
post.save()

# Creation of a Comment
comment = Comments(content="R u serious ?", user_id=user.id, post_id=post.id)
comment.save()

# Creation of a question 
question = Question(text="Tell me about yourself", type="RH", sub_id=sub.id, int_id=interview.id)
question.save()

# Creation of an Answer

ans = Answer(text="Bla bla bla", audio=None, int_id=interview.id)
ans.save()

models.storage.save()
