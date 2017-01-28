from app import app
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm

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

@app.route('/login/', methods=['GET','POST'])
def login():
	form = LoginForm() # this is being depreciated, need to fix
	
	if form.validate_on_submit():
		flash('Login request for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
		return redirect(url_for('index'))
	
	return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])