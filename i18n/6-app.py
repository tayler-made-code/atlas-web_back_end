#!/usr/bin/env python3

""" basic Flask app in 6-app.py """

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


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
    if 'locale' in request.args and \
            request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """ render a template """
    return render_template('6-index.html')


def get_user(user_id):
    """ returns a user dictionary or None if ID cannot be found """
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    return users.get(int(user_id))


@app.before_request
def before_request():
    """ """
    user_id = request.args.get('login_as', None)
    if user_id:
        flask.g.user = get_user(user_id)
    else:
        flask.g.user = None


@babel.timezoneselector
def get_timezone():
    if 'timezone' in request.args:
        try:
            pytz.timezone(request.args['timezone'])
            return request.args['timezone']
        except UnknownTimeZoneError:
            pass

    user = getattr(g, 'user', None)
    if user is not None and 'timezone' in user:
        try:
            pytz.timezone(user['timezone'])
            return user['timezone']
        except UnknownTimeZoneError:
            pass

    return 'UTC'
