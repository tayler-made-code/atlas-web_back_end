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


def _generate_uuid() -> str:
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

    def create_session(self, email: str) -> str:
        """ Method that takes an email string argument and returns the session
            ID as a string.
        """
        user = self._db.find_user_by(email=email)
        if not user:
            raise ValueError('User {} doesn\'t exist'.format(email))

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Method that takes a single session_id string argument and returns
            the corresponding User or None """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Method that takes a single user_id integer argument and returns
            None.
        """
        if user_id is None:
            return None

        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Method that takes an email string argument and returns a string.
        """
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                raise ValueError

            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token

        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Method that takes reset_token string argument and a password
            string argument and returns None.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if not user:
                raise ValueError

            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password,
                                 reset_token=None)

        except NoResultFound:
            raise ValueError
