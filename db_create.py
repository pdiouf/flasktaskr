# project/db_create.py


# import sqlite3
# from _config import DATABASE_PATH

# with sqlite3.connect(DATABASE_PATH) as connection:

# 	# get a cursor object to execute SQLcommands
# 	c = connection.cursor()

# 	# create the table

# 	c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		name TEXT NOT NULL, due_date NOT NULL, priority INTEGER NOT NULL,
# 		status INTEGER NOT NULL) """)

# 	c.execute(
# 		'INSERT INTO tasks (name, due_date, priority, status)' 
# 		'VALUES("Finish this tutorial", "03/25/2015", 10, 1)'
# 	)

# 	c.execute(
# 		'INSERT INTO tasks (name, due_date, priority, status)' 
# 		'VALUES("Finish Real Python Course 2", "03/25/2015", 10, 1)'
# 	)

from views import db
from models import Task
from datetime import date

# create the databasse and the db yable
db.create_all()

#insert data

db.session.add(Task("Finish this tutorial", date(2016, 9, 22), 10, 1))
db.session.add(Task("Finish Real Python", date(2016, 10, 3), 10, 1))

# commit the change
db.session.commit()
