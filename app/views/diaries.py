from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.models.diaries import Diary
from app.views.users import login_manager

login_manager.login_view = 'users.login'

diary_blueprint = Blueprint('diaries', __name__)


@diary_blueprint.route('/')
@login_required
def index():
    user_id = current_user.get_id()
    diaries = Diary.query.filter_by(user_id=user_id).order_by(Diary.created_date.desc()).all()

    return render_template('diaries/index.html', diaries=diaries)


@diary_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_diary():
    if request.method == 'POST' and 'title' in request.form:
        user_id = current_user.get_id()
        title = request.form.get('title')
        description = request.form.get('description')
        link = request.form.get('link')
        diary = add_diary_to_db(user_id, title, description, link)

        flash(f'Diary entry {diary.title} added')

        return redirect(url_for('diaries.index'))

    return render_template('diaries/add.html')


@diary_blueprint.route('/edit/<string:diary_id>', methods=['GET', 'POST'])
@login_required
def edit_diary(diary_id):
    diary = load_diary(diary_id)
    if request.method == 'POST':
        diary.title = request.form.get('title')
        diary.description = request.form.get('description')
        diary.link = request.form.get('link')
        db.session.commit()
        flash('Diary entry updated')

        return redirect(url_for('diaries.index'))

    return render_template('diaries/edit.html', diary=diary)


@diary_blueprint.route('/delete/<string:diary_id>', methods=['GET', 'POST'])
@login_required
def delete_diary(diary_id):
    diary = load_diary(diary_id)
    db.session.delete(diary)
    db.session.commit()

    return redirect(url_for('diaries.index'))


def add_diary_to_db(user_id, title, description, link):
    # noinspection PyArgumentList
    diary = Diary(user_id=user_id, title=title, description=description, link=link)
    db.session.add(diary)
    db.session.commit()
    flash('Diary entry created')

    return diary


def load_diary(diary_id):
    diary = Diary.query.filter_by(id=diary_id).first()

    return diary
