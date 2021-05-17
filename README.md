# FlaskTaskr

TaskFlasr is a Task Management system using Flask.

This project is from the [Real Python Course](https://realpython.com/products/real-python-course/)

### Install
```
# Create virtual environment
$ python3 -m venv venv

# Activate the virtual environment
$ source ./venv/scripts/activate

# Install the dependencies
$ pip install -r requirements.txt
```

### Setup

Create the _config.py file in the project directory with the following content:
```
import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktakr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret-key'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
```

### Run
```
# Run the application
$ python blog.py
```
