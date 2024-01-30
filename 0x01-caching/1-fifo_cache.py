#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Fifo class inherit from BaseCache class"""
    def __init__(self):
        """Class constructor"""
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """Add item into a cache
        Args:
            key(str): key of the item to add
            item(str): item to add
        Return: None
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.cache_data_list[0])
                deleted = self.cache_data_list.pop(0)
                print("DIACARD: {}".format(deleted))

    def get(self, key):
        """Retrieve an item from a cache
        Args:
            key(str): Key of the item to add
        Return: Item, if the key exist, none if otherwise
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
