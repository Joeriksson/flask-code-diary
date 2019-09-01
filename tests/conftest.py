import pytest

from app import create_app
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
    flask_app = create_app()

    test_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield test_client

    ctx.pop()
