from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


def create_app():
    flask_app = Flask(__name__)
    return flask_app


app = create_app()


db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site_user.db'
app.secret_key = os.urandom(12)

from app import routes
from app.models import users
