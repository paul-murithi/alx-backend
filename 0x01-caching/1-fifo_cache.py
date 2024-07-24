#!/usr/bin/env python3
""" Inherits from BaseCaching and is a caching system"""

BasicCache = __import__('0-basic_cache').BasicCache


class FIFOCache(BasicCache):
    """
    A caching system class that implements FIFO cache replacement policy
    """
    def __init__(self):
        """Initializes the FIFOCache"""
        super().__init__()

    def put(self, key, item):
        """Adds value to cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BasicCache.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            first_key = keys[0]
            self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Returns cache value at specified key"""
        return self.cache_data.get(key, None)
