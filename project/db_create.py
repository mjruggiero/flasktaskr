# project/db_create.py

from views import db
from models import Task, User
from datetime import date

# create the database and the db table
db.create_all()

db.session.add(User("admin", 'admin_admin.com', 'admin'))

# insert data
db.session.add(Task("Finish this tutorial", date(2016, 9, 22), 10, date(2016, 9, 22), 1, 1))
db.session.add(Task("Finish Real Python", date(2016, 10, 3), 10, date(2016, 10, 3), 1, 1))

# commit the changes
db.session.commit()
