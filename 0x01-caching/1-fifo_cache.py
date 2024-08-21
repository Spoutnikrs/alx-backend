#!/usr/bin/python3
"""
FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
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
        """
        Add an item in the cache using FIFO algorithm
        """
        if not key or not item:
            return

        if key not in self.cache_data and len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the first item added (FIFO)
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        # Update cache and order
        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
