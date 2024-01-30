#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
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
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                popped = self.cache_data_list.pop(0)
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
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
                return self.cache_data[key]
        return None
