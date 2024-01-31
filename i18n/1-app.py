#!/usr/bin/env python3

""" basic Flask app in 0-app.py """

from flask import Flask, render_template, Babel

app = Flask(__name__)

""" Create a single / route and an index.html template that simply outputs """
@app.route('/')
def hello_world():
    """ render a template """
    return render_template('1-index.html')

babel = Babel(app)
class Config(object):
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]

app.config.from_object('1-app.Config')

if __name__ == "__main__":