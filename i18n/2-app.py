#!/usr/bin/env python3

""" basic Flask app in 2-app.py """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
  """Config class for Babel"""
  LANGUAGES = ["en", "fr"]
  BABEL_DEFAULT_LOCALE = "en"
  BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
  """ determine the best match with supported languages """
  return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
  """ render a template """
  return render_template('2-index.html')
