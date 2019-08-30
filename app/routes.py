from app import app
from app.views.users import user_blueprint

from flask import render_template


app.register_blueprint(user_blueprint, url_prefix='/users')


@app.route('/')
def index():
    return render_template('index.html')

