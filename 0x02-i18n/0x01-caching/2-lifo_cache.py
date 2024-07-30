#!/usr/bin/env python3
""" Inherits from BaseCaching and is a caching system"""

BasicCache = __import__('0-basic_cache').BasicCache


class LIFOCache(BasicCache):
    """
    A caching system class that implements LIFO cache replacement policy
    """
    def __init__(self):
        """Initializes the LIFOCache"""
        super().__init__()

    def put(self, key, item):
        """Adds value to cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BasicCache.MAX_ITEMS:
                last_key, cache_val = self.cache_data.popitem()
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """Returns cache value at specified key"""
        return self.cache_data.get(key, None)
