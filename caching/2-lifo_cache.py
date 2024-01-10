#!/usr/bin/env python3

""" Create a class LIFOCache that inherits from BaseCaching and
    is a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Create a class LIFOCache that inherits from BaseCaching and
        is a caching system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            return
        if len(self.cache_data.keys()) >= self.MAX_ITEMS:
            discard = self.queue.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
