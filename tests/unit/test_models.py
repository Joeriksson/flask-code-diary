def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed password, authenticated
    """
    assert new_user.username == "test_user"
    assert new_user.email == "test@test.com"
    assert new_user.password != "abc123"


def test_new_diary_entry(new_diary):
    """
    GIVEN a Diary model
    WHEN a new Diary entry is created
    THEN check the title, description, link and user_id
    """
    assert new_diary.title == "My test diary entry"
    assert new_diary.description == "Description of the test diary entry"
    assert new_diary.link == "https://joeriksson.io"
