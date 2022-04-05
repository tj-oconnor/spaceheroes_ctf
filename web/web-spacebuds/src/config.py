"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

TESTING = True
DEBUG = True
FLASK_ENV = 'development'
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'