#!/usr/bin/env python3
"""
Module for interacting with PyMongo
"""

from pymongo import MongoClient


def log_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Display methods statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    # Display status check statistics
    status_check_count = collection.count_documents
    ({"method": "GET", "path": "/status"})
    print(f"status check: {status_check_count}")

    # Display top 10 IPs
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in top_ips:
        print(f"    {ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()        
