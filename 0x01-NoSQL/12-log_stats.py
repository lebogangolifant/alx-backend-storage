#!/usr/bin/env python3
"""
Provides statistics about Nginx logs
stored in MongoDB
"""
from pymongo import MongoClient


def nginx_log_stats():
    """
    Display statistics about Nginx logs stored in MongoDB:
    - Total number of logs
    - Count of each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Count of status check (GET requests to "/status")
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f'{total_logs} logs')

    # Count of each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    # Count of status check (GET requests to "/status")
    status_check = nginx_collection.count_documents
    ({"method": "GET", "path": "/status"})
    print(f'{status_check} status check')


if __name__ == "__main__":
    nginx_log_stats()
