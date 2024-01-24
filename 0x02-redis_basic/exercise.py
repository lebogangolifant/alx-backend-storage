#!/usr/bin/env python3
"""
Module Description: Implementation of the Cache class using Redis.
"""

import redis
import uuid
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method stores the input data
        in Redis using a random key and returns the key.

        Args:
        - data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
        - str: The randomly generated key used for storage.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
