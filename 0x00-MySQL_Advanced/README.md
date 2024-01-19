# 0x00. MySQL advanced

This directory contains MySQL projects focused on advanced database management. Each task explores various aspects of MySQL, including triggers, stored procedures, indexing, and other relevant topics.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [0-init.sql](0x00-MySQL_Advanced/0-init.sql)** - Initial setup for MySQL database and basic table creation.
- **Task 1: [1-conditional_trigger.sql](0x00-MySQL_Advanced/1-conditional_trigger.sql)** - Create a trigger that updates a column based on a condition.
- **Task 2: [2-update_quantity.sql](0x00-MySQL_Advanced/2-update_quantity.sql)** - Create a trigger to update quantity after inserting new orders.
- **Task 3: [3-total_quantity.sql](0x00-MySQL_Advanced/3-total_quantity.sql)** - Create a stored procedure to calculate the total quantity for each item.
- **Task 4: [4-decrease_quantity_on_order.sql](0x00-MySQL_Advanced/4-decrease_quantity_on_order.sql)** - Create a trigger to decrease the quantity of an item after adding a new order.
- **Task 5: [5-reset_valid_email.sql](0x00-MySQL_Advanced/5-reset_valid_email.sql)** - Create a trigger to reset the valid_email attribute only when the email has been changed.
- **Task 6: [6-add_bonus_correction.sql](0x00-MySQL_Advanced/6-add_bonus_correction.sql)** - Create a stored procedure to add a new correction for a student.
- **Task 7: [7-compute_average_score.sql](0x00-MySQL_Advanced/7-compute_average_score.sql)** - Create a stored procedure to compute and store the average score for a student.
- **Task 8: [8-index_my_names.sql](0x00-MySQL_Advanced/8-index_my_names.sql)** - Create an index on the first letter of the name in the 'names' table.
- **Task 9: [9-index_name_score.sql](0x00-MySQL_Advanced/9-index_name_score.sql)** - Create an index on the first letter of the name and the score in the 'names' table.
- **Task 10: [10-div.sql](0x00-MySQL_Advanced/10-div.sql)** - Create a function `SafeDiv` that safely divides two numbers.
- **Task 11: [11-need_meeting.sql](0x00-MySQL_Advanced/11-need_meeting.sql)** - Create a view listing students needing a meeting based on their scores and last meeting dates.
- **Task 12: [100-average_weighted_score.sql](0x00-MySQL_Advanced/100-average_weighted_score.sql)** - Create a stored procedure to compute and store the average weighted score for a specific student.
- **Task 13: [101-average_weighted_score.sql](0x00-MySQL_Advanced/101-average_weighted_score.sql)** - Create a stored procedure to compute and store the average weighted score for all students.

## Overview Concepts

The tasks in this directory cover the following MySQL concepts:

- Triggers and stored procedures.
- Indexing and optimizing database performance.
- Creating views for data retrieval.
- Working with functions and procedures.
- Handling complex queries and calculations.
- ...

## Requirements

- MySQL 5.7 (version 5.7.30)
- Ubuntu 18.04 LTS
- MySQL Database Server
- MySQL Client

## Setup

1. Install MySQL:

```bash
sudo apt update
sudo apt install mysql-server
```

2. Connect to MySQL and execute SQL scripts:

```bash
mysql -u username -p < script.sql
```

## Usage

To run each task, execute the corresponding SQL script or use the MySQL client to interact with the database.

- Example for Task 0:

```bash
mysql -u username -p < 0-init.sql
```

Feel free to explore each task for more details and specific instructions.

