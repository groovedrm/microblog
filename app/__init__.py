from flask import Flask

# Assigning the flask instance to app
app = Flask(__name__)

# Putting this here so we can avoid a circular reference.
# In other words, views is imported from the app variable above
from app import views