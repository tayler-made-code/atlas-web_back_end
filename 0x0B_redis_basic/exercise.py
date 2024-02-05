#!/usr/bin/env python3

""" Cache Class """

import redis
from typing import Union, Callable
import uuid


class Cache:
    """ Cache class """

    def __init__(self):
        """ Contructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """

        """ Generate a random key """
        key = str(uuid.uuid4())

        """ Store the data in Redis using the key """
        if isinstance(data, str):
            self._redis.set(key, data)
        elif isinstance(data, bytes):
            self._redis.set(key, data)
        elif isinstance(data, int):
            self._redis.set(key, str(data))
        elif isinstance(data, float):
            self._redis.set(key, str(data))

        return key
    
    def get(self, key: str, fn: callable) -> Union[str, bytes, None]:
        """ Automatically parametrize the return type """
        value = self._redis.get(key)
        return value.decode('utf-8') if value else None

    def get_str(self, key: str, fn: callable) -> Union[str, None]:
        """ Automatically parametrize the return type """
        value = self._redis.get(key)
        return value.decode('utf-8') if value else None

    def get_int(self, key: str, fn: callable) -> Union[int, None]:
        """ Automatically parametrize the return type """
        value = self._redis.get(key)
        return int(value.decode('utf-8')) if value else None
