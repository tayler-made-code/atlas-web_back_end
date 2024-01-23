#!/usr/bin/env python3

""" Auth module """
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Instance of the Auth class """
        self._db = DB()

    @staticmethod
    def _hash_password(password: str) -> bytes:
        """ Method that takes in a password string arguments and returns bytes.
        """
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password

    def register_user(self, email: str, password: str) -> User:
        """ Method that takes mandatory email and password string arguments
            and returns a User object.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)
