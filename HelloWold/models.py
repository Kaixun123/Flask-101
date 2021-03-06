from datetime import datetime
''' 
    serialization/serialisation is the process of translating data structure or object 
    state into a format that can be stored or transmitted and reconstructed later.
'''
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from HelloWold import db, login_manager
from flask import current_app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

# model for the user information (username, email, password, etc.)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    #backref used to get match the author of post with the user
    #lazy will help SQLalchemy load all the data as necessary in one go, more convience 
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        # set the secret key and expiry time
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        # return a token and a payload with user id
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    #magic method (double underscore method)
    #how our object is printed when we print out 
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# db.column is to create a new column into the database
# model for the post (title, id, content, etc.)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # 1:M relationship between the user and post
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
