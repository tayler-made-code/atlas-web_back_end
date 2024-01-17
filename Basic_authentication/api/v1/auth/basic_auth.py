#!/usr/bin/env python3

""" Basic Auth """

from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """ basic auth class """

    def __init__(self):
        """ init """
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract base64 auth header """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ decode base64 auth header """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return base64_authorization_header.decode('utf-8')
        except Exception:
            return None
