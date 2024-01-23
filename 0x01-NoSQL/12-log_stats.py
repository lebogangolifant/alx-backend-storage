#!/usr/bin/env python3
"""
Module that log stats
"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Display stats about Nginx logs stored in MongoDB

    Args:
        mongo_collection: pymongo collection object
    """
    total_logs = mongo_collection.count_documents({})
    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print("method {}: {}".format(method, count))

    status_check_count = mongo_collection.count_documents
    ({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    """
    Database: logs
    Collection: nginx
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    log_stats(logs_collection)
