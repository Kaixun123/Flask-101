#import flask into this .py file
#url4 is a flask function find the exact number of routes for us
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

#create a app variable, __name__ is the module used 
app = Flask(__name__) 

#to get the secret key:
# python -> import secrets -> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'c3352fc50a12c11f08c9861576e2417365e3ff283b75c0fea52dece3ddca5fc8'

#database with Flask-SQLAlchemy, we will be using a SQLite database for development 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# can represent our db structure as classes/models
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_POST'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kai.xun.development@gmail.com'
app.config['MAIL_PASSWORD'] = ''
mail = Mail(app)
#enter password every time to see if it works

from hellowold import routes
