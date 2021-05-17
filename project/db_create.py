# project/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    # get a curcor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE tasks(
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        due_date TEXT NOT NULL,
        priority INTEGER NOT NULL,
        status TEXT NOT NULL
        )""")

    # insert dummy data into database
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES ("Finish this tutorial", "3/25/2015", 10, 1)'
    )

    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES ("Finish Real Python Course 2", "3/25/2015", 10, 1)'
    )
