#!/usr/bin/env python3
""" Module for interacting with PyMongo """

from pymongo.collection import Collection
from typing import List


def top_students(mongo_collection: Collection) -> List[dict]:
    """
    Returns all students from the MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection)

    Returns:
        List[dict]: A list of all student documents in the collection.
    """
    return list(mongo_collection.find())
