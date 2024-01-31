#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class inherit from BaseCache class"""
    def __init__(self):
        """Class constructor"""
        super().__init__()
        self.cache_data_order = []

    def put(self, key, item):
        """Add item into a cache
        Args:
            key(str): key of the item to add
            item(str): item to add
        Return: None
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_order:
                self.cache_data_order.append(key)
            else:
                self.cache_data_order.remove(key)
                self.cache_data_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                length = len(self.cache_data_order)
                popped = self.cache_data_order.pop(length - 2)
                del self.cache_data[popped]
                print("DISCARD: {}".format(popped))

    def get(self, key):
        """Retrieve an item from a cache
        Args:
            key(str): Key of the item to add
        Return: Item, if the key exist, none if otherwise
        """
        if key:
            if key in self.cache_data:
                self.cache_data_order.remove(key)
                self.cache_data_order.append(key)
                return self.cache_data[key]
        return None
