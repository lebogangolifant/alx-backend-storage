#!/usr/bin/env python3
"""
Module that Cache class using Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator counts the number of times a method is called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper method
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs
    and outputs for a function in Redis.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper method
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


class Cache:
    """
    Represents a cache using Redis.
    """

    def __init__(self) -> None:
        """
        Method that initialise the Cache instance
        with a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method stores the input data
        in Redis using a random key and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """
        Method retrieves data from Redis
        using a key and applies the optional conversion function.
        """
        data = self._redis.get(key)
        if data is None:
            return data

        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Method retrieves a string from Redis using a key.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Method retrieves an integer from Redis using a key.
        """
        return self.get(key, fn=int)
