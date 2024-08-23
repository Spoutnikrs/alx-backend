#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    caching system using the LRU algorithm
    """

    def __init__(self):
        """
        initialize the LRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
