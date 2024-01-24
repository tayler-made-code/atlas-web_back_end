#!/usr/bin/env python3

""" Auth module """
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Method that takes in a password string arguments and returns bytes.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Instance of the Auth class """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method that takes mandatory email and password string arguments
            and returns a User object.
        """
        try:
            users = self._db.find_user_by(email=email)
            if users:
                raise ValueError('User {} already exists'.format(email))

        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)