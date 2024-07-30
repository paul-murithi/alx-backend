#!/usr/bin/env python3
""" Inherits from BaseCaching and is a caching system"""

BasicCache = __import__('0-basic_cache').BasicCache


class MRUCache(BasicCache):
    """
    A caching system class that implements MRU cache replacement policy
    """
    def __init__(self):
        """Initializes the MRUCache"""
        super().__init__()
        self._keys = []

    def put(self, key, item):
        """Adds value to cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self._keys.remove(key)

        else:
            if len(self.cache_data) + 1 > BasicCache.MAX_ITEMS:
                old_key = self._keys.pop()
                del self.cache_data[old_key]
                print("DISCARD: {}".format(old_key))
        self._keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Returns cache value at specified key"""
        if not key or key not in self.cache_data:
            return None
        self._keys.remove(key)
        self._keys.append(key)
        return self.cache_data.get(key, None)
