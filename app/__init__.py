import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config_filename=None):
    if config_filename:
        flask_app = Flask(__name__, instance_relative_config=True)
        flask_app.config.from_pyfile(config_filename)
        initialize_extensions(flask_app)
    else:
        flask_app = Flask(__name__)

    return flask_app


def initialize_extensions(app):
    db.init_app(app)


app = create_app()


db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site_user.db'
app.secret_key = os.urandom(12)

from app import routes

