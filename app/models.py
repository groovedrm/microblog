from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	
	# This last one is not an actual field. It defines a 1-to-many relationship
	# It is a data member (user.posts) that provides a list of posts
	# from a particular user
	
	# backref defines the field that will be added to the posts pointing
	# back to an individual user
	
	def _repr__(self):
		# this method tells Python how to print the object (User)
		return '<User %s>' % str(self.nickname)
		
	# NEED TO RESOLVE BELOW WARNING related to function
	# compiler.py:624: SAWarning: Can't resolve label reference 'nickname desc'; converting to text() 
	# (this warning may be suppressed after 10 occurrences
		
class Post (db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	# Foreign key from the user class above
	# but have to remember to keep the format the same
	# otherwise it is not useful for the data relationship)
	
	
	def __repr__(self):
		return '<Post %r>' % (self.body)
		