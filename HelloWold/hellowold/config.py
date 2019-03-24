import os

class Config:
    # to get the secret key:
    # python -> import secrets -> secrets.token_hex(16)
    # creating environment variables from the computer to prevent the sensitive information from being released
    SECRET_KEY = os.environ.get('secrets_key')
    # database with Flask-SQLAlchemy, we will be using a SQLite database for development
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_POST = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kai.xun.development@gmail.com'
    MAIL_PASSWORD = ''
    # enter password every time to see if it works
