"""
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
"""


class Config:
    """Base config"""

    FLASK_APP = 'main.py'

    SECRET_KEY = ''  # generate yours

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db\\db.db'  # example

    SERVER_NAME = ''  # domain name

    # also, you can add here another global constant of different modules


class DevConfig(Config):
    TESTING = False
    DEBUG = True

    SQLALCHEMY_ECHO = True


# creare another config
