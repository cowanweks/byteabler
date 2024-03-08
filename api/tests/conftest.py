import pytest
from flask_app import create_app
from app.extensions import db, jwt, sess
from app.flask_config import TestingConfig
from flask_jwt_extended import create_access_token


@pytest.fixture()
def app():
    flask_app = create_app()
    flask_app.config.from_object(TestingConfig)

    db.init_app(flask_app)
    jwt.init_app(flask_app)
    sess.init_app(flask_app)

    with flask_app.app_context():
        db.create_all()

    yield flask_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def access_token(app):
    with app.app_context():
        return f"Bearer {create_access_token(identity='cowanweks')}"


@pytest.fixture
def create_test_user(client):

    headers = {
        "Content-Type": "application/json"
    }

    user_data = {
        'staff_no': 'STF-0001',
        "username": "cowanweks",
        "password": "cowanweks",
        "confirm_password": "cowanweks",
        "role_id": "R-001"
    }

    response = client.post("/api/users/new",
                           headers=headers, json=user_data)

    if response.status_code == 201:
        return user_data, response.status_code
    return None, response.status_code


@pytest.fixture
def signin_test_user(client, access_token, create_test_user):

    user_data, _ = create_test_user

    assert _ == 201
    assert user_data is not None

    headers = {
        "Content-Type": "application/json"
    }

    response = client.post("/api/users/signin",
                           headers=headers, json=user_data)

    if response.status_code == 200:
        return user_data, access_token, response.status_code

    return None, None, response.status_code
