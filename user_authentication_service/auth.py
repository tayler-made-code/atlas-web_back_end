#!/usr/bin/env python3

import bcrypt

def _hash_password(password):
    if isinstance(password, str):
        password = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password
