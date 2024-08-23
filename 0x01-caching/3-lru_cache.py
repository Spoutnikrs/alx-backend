#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    caching system using the LRU algorithm
    """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):

        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self._update_order(key)

    def get(self, key):
        if key in self.cache_data:
            self._update_order(key)
            return self.cache_data[key]
        return None

    def _update_order(self, key):
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
