""" setup a basic Flask app in 0-app.py. Create a single / route and an 
    index.html template that simply outputs “Welcome to Holberton” as
    page title (<title>) and “Hello world” as header (<h1>) """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ return a simple string for starters """
    return 'Hello HBNB!'
