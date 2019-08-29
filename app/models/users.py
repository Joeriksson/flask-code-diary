from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    firstname = db.Column(db.String(100), unique=False)
    lastname = db.Column(db.String(100), unique=False)
    email = db.Column(db.String(100))

    def __repr__(self):
        return f'User {self.username}'