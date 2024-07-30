#!/usr/bin/env python3
""" Inherits from BaseCaching and is a caching system"""

BasicCache = __import__('0-basic_cache').BasicCache


class LFUCache(BasicCache):
    """
    A caching system class that implements LRU cache replacement policy
    """
    def __init__(self):
        """Initializes the LFUCache"""
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """Adds value to cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1

        elif len(self.cache_data) + 1 > BasicCache.MAX_ITEMS:
            lfu_key = min(self.freq, key=self.freq.get)
            del self.cache_data[lfu_key]
            del self.freq[lfu_key]
            print("DISCARD: {}".format(lfu_key))
        self.cache_data[key] = item
        self.freq[key] = self.freq.get(key, 0) + 1

    def get(self, key):
        """Returns cache value at specified key"""
        if key in self.cache_data:
            self.freq[key] = self.freq.get(key, 0) + 1
        return self.cache_data.get(key)
