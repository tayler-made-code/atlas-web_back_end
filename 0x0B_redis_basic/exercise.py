#!/usr/bin/env python3

""" Cache Class """

import redis
from typing import Union, Callable, Optional, Any
from functools import wraps, cache
import uuid


def count_calls(method: Callable) -> Callable:
    """ Stores the number of calls to a method """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ use the qualified method name as a key """
        key = method.__qualname__

        """ increment the key in redis  using incr command """
        self._redis.incr(key)

        """ call the method and return the result """
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and outputs for a method """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Use the qualified method name as a key """
        key = method.__qualname__

        """ Create the input and output list keys """
        input_list_key = key + ":inputs"
        output_list_key = key + ":outputs"

        """ append the input arguments to the input list in Redis """
        self._redis.rpush(input_list_key, str(args))

        """ execute the wrapper function """
        result = method(self, *args, **kwargs)

        """ store the output in the output list in Redis """
        self._redis.rpush(output_list_key, str(result))

        """ return the output """
        return result

    return wrapper


def replay(method: Callable) -> None:
    """ display the history of calls of a particular function """
    
    """ Get the qualified method name """
    key = method.__qualname__

    input_list_key = key + ":inputs"
    output_list_key = key + ":outputs"

    """ get the input and output histories from Redis """
    inputs = cache._redis.lrange(input_list_key, 0, -1)
    outputs = cache._redis.lrange(output_list_key, 0, -1)

    """ print the number of calls """
    print(f"{key} was called {len(inputs)} times:")

    """ iterate over the inputs and the outputs and print them """
    for i, (input_str, output_str) in enumerate(zip(inputs, outputs)):
        """ decode the input and output from bytes to str """
        input_tuple = eval(input_str.decode('utf-8'))
        output_key = output_str.decode('utf-8')

        """ format and print the input and output """
        print(f"{key}(*{input_tuple}) -> {output_key}")


class Cache:
    """ Cache class """

    def __init__(self):
        """ Contructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Get data from redis with an optional callback function """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """ Automatically parametrize the return type """
        if key is None:
            return None
        value = self.get(key)
        if value is not None:
            return value.decode('utf-8')
        return value

    def get_int(self, key: str) -> Union[int, None]:
        """ Automatically parametrize the return type """
        if key is None:
            return None
        value = self.get(key)
        if value is not None:
            try:
                return int(value)
            except Exception as e:
                raise ValueError(f"Value at {key} is not an integer") from e
        return None
