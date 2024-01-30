#!/usr/bin/env python3
"""Create a class BasicCache that inherits from BaseCaching and
is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching System"""
    def __init__(self):
        """Initialize class instance"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add an item to the caching system
        Args:
            key(str): key of the item to be added
            item(str): item to be added to the cache
        Return: None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get or retrieve item from the cache
        Args:
            key(str): Key of the item to be retrieved
        Return: Item associated with the key or none if otherwise
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
