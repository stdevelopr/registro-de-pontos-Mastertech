"""Flask configuration variables."""
from os import environ, path
db_path = path.join(path.dirname(__file__), 'instance/flaskr.sqlite')
db_uri = 'sqlite:///{}'.format(db_path)

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False