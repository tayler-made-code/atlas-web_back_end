#!/usr/bin/env python3
""" function that lists all documents in a collection """
import pymongo


def list_all(mongo_collection):
    """ return an empty list if no document in the collection
        otherwise list all the documents in the collection """
    if mongo_collection is not None:
        return list(mongo_collection.find())
    return []
