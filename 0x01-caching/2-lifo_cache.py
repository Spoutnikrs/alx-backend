#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        Caching system using the FIFO algorithm
        """

    def __init__(self):
        """
        Initialize the FIFOCache
        """
        super().__init__()

        # To keep track of the order in which items are added
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using the LIFO algorithm
        """
        if not key or not item:
            return

        if key not in self.cache_data and len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the most recent item added (LIFO)
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        # Add or update the cache
        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
