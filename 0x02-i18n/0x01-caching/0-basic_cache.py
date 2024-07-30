#!/usr/bin/env python3
""" BasicCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """
        Assigns an item value for the key to dictionary
        Args:
            key: Dictionary key to assign the value
            item: Value to add to dictionary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets the cache value as the the key
        Args:
           key: The key to cache value
        """
        return self.cache_data.get(key, None)
