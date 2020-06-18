#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask, render_template
from models import storage
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
from web_flask import app

@app.route('/')
@app.route('/home')
def hello_hbnb():
    """ Prints a Message when / is called """
    
    users = storage.all(User).values()
    posts = storage.all(Post).values()
    comments = storage.all(Comments).values()
    return render_template('home.html', users=users, posts=posts, coms=comments)


@app.route('/login')
def login():
    """go to login"""
    return render_template('login.html')


@app.route('/signup')
def signup():
    """ signup  """
    return render_template('signup.html')


@app.route('/contact_us')
def contact_us():
    """contact us"""
    return render_template('contact_us.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)