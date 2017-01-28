import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'MyGuess'

# First line activates cross site forgery request
# Needed when CSFR is enabled, and is used to validate a form

OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
	{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
	{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# The URI line is required by the Flask SQL alchemy extension. It is the
# database file path

# The repo line is where we store database migrate files