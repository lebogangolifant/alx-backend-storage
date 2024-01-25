# 0x02. Redis basic

This directory focuses on Redis, covering basic operations and usage as a simple cache. The tasks explore Redis commands, Redis Python client, and provide a Redis crash course tutorial.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [exercise.py](0x02-redis_basic/exercise.py)** - Implement a Cache class with Redis as a backend. Create a store method to store data in Redis and return a generated random key.
- **Task 1: [exercise.py](0x02-redis_basic/exercise.py)** - Implement a get method that retrieves data from Redis, with optional conversion using a Callable argument.
- **Task 2: [exercise.py](0x02-redis_basic/exercise.py)** - Implement a count_calls decorator to count the number of times methods of the Cache class are called.
- **Task 3: [exercise.py](0x02-redis_basic/exercise.py)** - Create a call_history decorator to store the history of inputs and outputs for a particular function.
- **Task 4: [exercise.py](0x02-redis_basic/exercise.py)** - Implement a replay function to display the history of calls of a particular function.
- **Task 5: [web.py](0x02-redis_basic/web.py)** - Implement a get_page function to obtain the HTML content of a URL using the requests module. Cache the result in Redis with a 10-second expiration.

## Overview Concepts

The tasks in this directory cover the following Redis basic concepts:

- Redis commands and basic operations.
- Redis Python client and its usage.
- Implementing decorators in Python for function tracking and history.
- Redis as a simple cache for efficient data storage.

## Requirements

- Python 3.7
- Redis
- Ubuntu 18.04 LTS
- pycodestyle 2.5

## Setup

1. Install Redis:

```bash
sudo apt update
sudo apt install redis-server
```

## Usage

To run each task, execute the corresponding Python script or use the provided examples (main.py) files in the test folder.

- Example for Task 0:

```bash
python3 main.py
```
