#!/usr/bin/env python3

""" Auth module """
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """ Method that takes in a password string arguments and returns bytes.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def _generate_uuid(self) -> str:
    """ Method that returns a string representation of a new UUID.
    """
    string_uuid = str(uuid.uuid4())
    return string_uuid


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Method that takes email and password string arguments and reutnrs
            a boolean.
        """
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                return False

            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True

        except NoResultFound:
            pass

        return False
