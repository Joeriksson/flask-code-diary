from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
import bcrypt
from app import app, db
from app.models.users import User


user_blueprint = Blueprint('users', __name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@user_blueprint.route('/')
def index():
    pass


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST' and 'username' in request.form:
        username = request.form.get('username')
        email = request.form.get('email')

        if validate_username(username) and validate_email(email):
            password = request.form.get('password')
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user = add_user(username, hashed, firstname, lastname, email)
            login_user(user)
            return render_template('index.html')

        flash('Username and/or email already exists. Please use a different username and/or email.')

    return render_template('users/register.html')


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form:
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user:
            if bcrypt.checkpw(request.form.get('password').encode('utf-8'), user.password):
                login_user(user)
                return redirect(url_for('index'))
        return 'Invalid username or password'

    return render_template('users/login.html')


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@user_blueprint.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_user():
    user = load_user(current_user.get_id())

    if request.method == 'POST':
        user.firstname = request.form.get('firstname')
        user.lastname = request.form.get('lastname')
        user.email = request.form.get('email')
        password = request.form.get('password')

        if password:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user.password = hashed

        db.session.commit()
        flash('Profile updated')
        return redirect(url_for('index'))

    return render_template('users/edit.html', user=user)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def add_user(username, password, firstname, lastname, email):
    # noinspection PyArgumentList
    user = User(username=username, password=password, firstname=firstname, lastname=lastname, email=email)
    db.session.add(user)
    db.session.commit()
    flash('User Created')
    return user


def validate_username(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return False
    return True


def validate_email(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return False
    return True

