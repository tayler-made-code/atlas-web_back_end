#!/usr/bin/env python3

""" Implement a hash_password function that expects one string argument name
    password and returns a salted, hashed password, which is a byte string

    Use the bcrypt package to perform the hashing (with hashpw) """

import bcrypt


def hash_password(password: str) -> bytes:
    """ hash_password returns a salted, hashed password, which is a byte string
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ is_valid returns a boolean """
    return bcrypt.checkpw(password.encode(), hashed_password)
