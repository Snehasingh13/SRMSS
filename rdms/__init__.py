from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta
import sqlite3


# Initialize flask app
app = Flask(__name__) 

# Set app secret key
# Keep this private!
app.secret_key = '1s5e1521def421s431d5'

# Change this URI if you are working with this project on your machine
# Configure database connection 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# Suppress warnings 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['pool_pre_ping'] = True

# Configure app to remember user login for 180 seconds on browser terminate
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=180)
app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True

# Attach SQLAlchemy to app 
db = SQLAlchemy(app)


from rdms import routes 
