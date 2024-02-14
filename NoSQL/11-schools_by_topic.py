#!/usr/bin/env python3
""" function that returns the list of school having a specific topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ returns schools with a specific topic """
    if mongo_collection is not None and topic is not None:
        return mongo_collection.find({"topics": topic})
    return []
