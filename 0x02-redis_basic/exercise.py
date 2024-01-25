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
        method_name = method.__qualname__

        input_key = f"{method_name}:inputs"
        input_str = str(args)
        self._redis.rpush(input_key, input_str)

        output = method(self, *args, **kwargs)

        output_key = f"{method_name}:outputs"
        output_str = str(output)
        self._redis.rpush(output_key, output_str)

        return output

    return wrapper


def replay(fn: Callable) -> None:
    """
    Display the history of calls for a particular function.
    """
    redis_client = redis.Redis()
    function_name = fn.__qualname__

    num_calls = redis_client.get(function_name)
    try:
        num_calls = num_calls.decode('utf-8')
    except AttributeError:
        num_calls = 0

    print(f'{function_name} was called {num_calls} times:')

    input_list = redis_client.lrange(function_name + ":inputs", 0, -1)
    output_list = redis_client.lrange(function_name + ":outputs", 0, -1)

    for input_args, output in zip(input_list, output_list):
        try:
            input_args = input_args.decode('utf-8')
        except AttributeError:
            input_args = ""
        try:
            output = output.decode('utf-8')
        except AttributeError:
            output = ""

        print(f'{function_name}(*{input_args}) -> {output}')


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
    @call_history
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
