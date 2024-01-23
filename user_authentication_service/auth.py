#!/usr/bin/env python3

""" Auth module """
import bcrypt


def _hash_password(password):
    """ Method that takes in a password string arguments and returns bytes.
    """
    if isinstance(password, str):
        password = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password
