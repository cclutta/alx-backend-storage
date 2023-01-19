#!/usr/bin/env python3
"""
Exercise module
"""

import redis
import uuid
from typing import Union, Callable, Optional



class Cache:
    """
    Class cache
    """
    def __init__(self) -> None:
        """
        Init redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in redis cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
