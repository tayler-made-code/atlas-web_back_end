#!/usr/bin/env python3

""" Basic Auth """

from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
import base64
from models.user import User


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
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('utf-8')
            return message
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ extract user credentials """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ user object from credentials """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        # Return None if your database (file) doesn’t contain any User instance with email equal to user_email - you should use the class method search of the User to lookup the list of users based on their email. Don’t forget to test all cases: “what if there is no user in DB?”, etc.
        try:
            # Return None if your database (file) doesn’t contain any User instance with email equal to user_email - you should use the class method search of the User to lookup the list of users based on their email. Don’t forget to test all cases: “what if there is no user in DB?”, etc.
            if User.search({'email': user_email}) == []:
                return None
        except Exception:
            return None
        

        # Return None if user_pwd is not the password of the User instance found - you must use the method is_valid_password of User
        try:
            """ Return None if user_pwd is not the password of the User instance found - you must use the method is_valid_password of User """
            if User.search({'email': user_email})[0].is_valid_password(user_pwd) is False:
                return None
        except Exception:
            return None
        """ Return the User instance otherwise """
        return User.search({'email': user_email})[0]
