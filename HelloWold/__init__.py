#import flask into this .py file
#url4 is a flask function find the exact number of routes for us

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from HelloWold.config import Config


# can represent our db structure as classes/models
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

#login_view is to make sure that the account is login before access any pages
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    # create a app variable, __name__ is the module used
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from HelloWold.users.routes import users
    from HelloWold.posts.routes import posts
    from HelloWold.main.routes import main
    from HelloWold.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app 
