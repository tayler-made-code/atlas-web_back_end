#!/usr/bin/env python3

""" Basic Auth """

from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
  """ basic auth class """
