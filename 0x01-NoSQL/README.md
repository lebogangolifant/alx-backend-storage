# 0x01. NoSQL

This directory contains NoSQL projects that focus on MongoDB database management. Each task explores various aspects of MongoDB, including basic operations, querying, and updates.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [0-list_databases](0x01-NoSQL/0-list_databases)** - Write a script that lists all databases in MongoDB.
- **Task 1: [1-use_or_create_database](0x01-NoSQL/1-use_or_create_database)** - Write a script that creates or uses the database `my_db`.
- **Task 2: [2-insert](0x01-NoSQL/2-insert)** - Write a script that inserts a document in the collection `school` of the database `my_db`.
- **Task 3: [3-all](0x01-NoSQL/3-all)** - Write a Python function that lists all documents in a MongoDB collection.
- **Task 4: [4-match](0x01-NoSQL/4-match)** - Write a script that displays all documents in the collection `school` where `name` is "Holberton school".
- **Task 5: [5-count](0x01-NoSQL/5-count)** - Write a script that displays the number of documents in the collection `school`.
- **Task 6: [6-update](0x01-NoSQL/6-update)** - Write a script that updates all documents in the collection `school` with the attribute `address` set to "972 Mission street".
- **Task 7: [7-delete](0x01-NoSQL/7-delete)** - Write a script that deletes all documents in the collection `school` where `name` is "Holberton school".
- **Task 8: [8-all](0x01-NoSQL/8-all)** - Write a Python function that lists all documents in a MongoDB collection.
- **Task 9: [9-insert_school](0x01-NoSQL/9-insert_school)** - Write a Python function that inserts a new document in a MongoDB collection based on kwargs.
- **Task 10: [10-update_topics](0x01-NoSQL/10-update_topics)** - Write a Python function that changes all topics of a school document based on the name.
- **Task 11: [11-schools_by_topic](0x01-NoSQL/11-schools_by_topic)** - Write a Python function that returns the list of schools having a specific topic.
- **Task 12: [12-log_stats.py](0x01-NoSQL/12-log_stats.py)** - Write a Python script that provides stats about Nginx logs stored in MongoDB.
- **Task 13: [100-find](0x01-NoSQL/100-find)** - Write a script that lists all documents with names starting by "Holberton" in the collection `school`.
- **Task 14: [101-students.py](0x01-NoSQL/101-students.py)** - Write a Python function that returns all students sorted by average score.
- **Task 15: [102-log_stats.py](0x01-NoSQL/102-log_stats.py)** - Improve `12-log_stats.py` by adding the top 10 of the most present IPs in the collection `nginx` of the database `logs`.

## Overview Concepts

- **Basic MongoDB Operations:**
  - Creation of databases and collections.
  - Insertion, updating, and deletion of documents.

- **Querying MongoDB:**
  - Retrieval of documents based on specific conditions.
  - Listing all documents in a collection.

- **Updating MongoDB Documents:**
  - Modification of document attributes.
  - Deletion of documents based on specific conditions.

- **Python Scripting for MongoDB:**
  - Execution of MongoDB scripts using Python.
  - Implementation of Python functions to interact with MongoDB.

- **MongoDB Statistics:**
  - Generation of statistics and insights from Nginx logs stored in MongoDB.

## Requirements

- Ubuntu 18.04 LTS
- pycodestyle 2.5.*
- MongoDB 3.6
- Python 3.6
- pymongo (Python library) 3.10

## Setup

1. Install MongoDB:

```bash
sudo apt update
sudo apt install mongodb
```

2. Install pymongo:

```bash
pip install pymongo
```

## Usage

To run each task, execute the corresponding script or Python function:

- Example for Task 0:

```bash
./0-list_databases | mongo
```

- Example for Task 3 (Python function):

```
cat 3-all | mongo my_db
```
