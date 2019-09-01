import bcrypt
from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    firstname = db.Column(db.String(100), unique=False)
    lastname = db.Column(db.String(100), unique=False)
    email = db.Column(db.String(100))
    diaries = db.relationship('Diary', backref='user', lazy=True)

    def __init__(self, username, password, firstname, lastname, email):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __repr__(self):
        return f'User {self.username}'
