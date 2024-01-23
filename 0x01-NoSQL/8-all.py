#!/usr/bin/env python3
"""
Module that list all documents in Python
"""


def list_all(mongo_collection):
    """
    List all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents in the collection
    """
    return list(mongo_collection.find())
