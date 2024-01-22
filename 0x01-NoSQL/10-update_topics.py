#!/usr/bin/env python3
"""
Module that Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of a school document based on the name

    Args:
        mongo_collection: pymongo collection object
        name: School name to update
        topics: List of topics approached in the school
    """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, update)
