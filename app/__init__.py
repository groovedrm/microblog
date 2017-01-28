from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Assigning the flask instance to app
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Putting this here so we can avoid a circular reference.
# In other words, views is imported from the app variable above
from app import views, models