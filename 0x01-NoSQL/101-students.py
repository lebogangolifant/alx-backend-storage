#!/usr/bin/env python3
"""
Module for interacting with PyMongo
"""


def top_students(mongo_collection):
    """
    Returns all students from the MongoDB collection
    """
    return list(mongo_collection.find())
