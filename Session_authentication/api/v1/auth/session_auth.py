#!/usr/bin/env python3

""" Session Auth """

from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth
import os

auth_type = os.getenv('AUTH_TYPE')
if auth_type == 'session_auth':
    auth = SessionAuth()
else:
    auth = Auth()


class SessionAuth(Auth):
    """ user id by session id class """
    pass
