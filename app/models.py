from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	
	def _repr__(self):
		# this method tells Python how to print the object (User)
		return '<User %r>' % (self.nickname)
		