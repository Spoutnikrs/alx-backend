#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines a caching system using the MRU algorithm """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm """
        if key and item:
            if key in self.cache_data:
                # Move the key to the most recent position
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the most recently used item
                mru_key = self.order.pop(-1)
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

            # Insert the new key as the most recent one
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            # Mark the key as most recently used
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
