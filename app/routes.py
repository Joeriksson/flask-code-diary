from flask import render_template

from app import app
from app.views.diaries import diary_blueprint
from app.views.users import user_blueprint

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(diary_blueprint, url_prefix='/diaries')


@app.route('/')
def index():
    return render_template('index.html')

