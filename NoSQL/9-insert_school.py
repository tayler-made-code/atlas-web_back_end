#!/usr/bin/env python3
""" function that inserts a new document in a collection based on kwargs """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ insert a new document in the collection based on kwargs """
    if mongo_collection is not None:
        new_doc = mongo_collection.insert_one(kwargs)
        return new_doc.inserted_id
    return None
