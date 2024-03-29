#!/usr/bin/env python3

""" basic Flask app in 1-app.py """

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

""" Create a single / route and an index.html template
    that simply outputs """


@app.route('/')
def hello_world():
    """ render a template """
    return render_template('1-index.html')
