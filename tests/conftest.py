import pytest

from app import create_app, db
from app.models.diaries import Diary
from app.models.users import User


@pytest.fixture(scope='module')
def new_user():
    user = User(username="test_user", password="abc123", email="test@test.com", firstname="Test", lastname="User")
    return user


@pytest.fixture(scope='module')
def new_diary():
    diary = Diary(
        title="My test diary entry",
        description="Description of the test diary entry",
        link="https://joeriksson.io",
    )
    return diary


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    test_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield test_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    user1 = User(username="test_user1", password="abc123", email="test1@test.com", firstname="Test1", lastname="User")
    user2 = User(username="test_user2", password="abc123", email="test2@test.com", firstname="Test2", lastname="User")
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    yield db

    db.drop_all()
