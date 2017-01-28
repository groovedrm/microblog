from app import app
from flask import render_template

@app.route('/')
@app.route('/index/')
def index ():
	user = {'nickname': 'Chris'}
	posts = [
		{
			'author': {'nickname': 'John'},
			'body': 'Beautiful day in New York!'
		},
		{
			'author': {'nickname': 'Chris'},
			'body': 'Beautiful day for Chris!'
		}
	]
	
	return render_template('index.html', title='Home', user=user, posts=posts)
