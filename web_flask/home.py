#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
from models import storage
from models.user import User
from models.post import Post

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/home')
def hello_hbnb():
    """ Prints a Message when / is called """
    
    users = storage.all(User).values()
    return render_template('home.html', data=users)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
