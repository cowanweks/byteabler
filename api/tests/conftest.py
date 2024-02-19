import pytest
from app import create_app
from app.extensions import db
from app.flask_config import TestingConfig
from flask_jwt_extended import JWTManager, create_access_token


@pytest.fixture()
def app():
    app = create_app()
    app.config.from_object(TestingConfig)
    db.init_app(app)
    JWTManager(app)

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def access_token(app):
    with app.app_context():
        return f"Bearer {create_access_token(identity='cowanweks')}"


@pytest.fixture
def create_test_user(client, access_token):

    headers = {
        'Authorization': access_token
    }

    user_data = {
        'staff_no': 'STF-0001',
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'a_secure_password',
        'confirm_password': 'a_secure_password',
        'role_id': 'R-001'
    }

    response = client.post("/api/users/new",
                           headers=headers, json=user_data)

    if response.status_code == 201:
        return user_data, response.status_code
    return None, response.status_code


@pytest.fixture
def create_test_role(client, access_token):

    headers = {
        'Authorization': access_token
    }

    role_data = {
        'role_id': 'ROLE-001',
        'role_name': 'Administrator'
    }

    response = client.post("/api/roles/new",
                           headers=headers, json=role_data)

    if response.status_code == 201:

        return role_data, response.status_code

    return None, response.status_code


@pytest.fixture
def create_test_unit(client, access_token):

    headers = {
        'Authorization': access_token
    }

    unit_data = {
        'unit_code': 'UNIT-001',
        'unit_name': 'Human Resources'
    }

    response = client.post("/api/units/new",
                           headers=headers, json=unit_data)

    if response.status_code == 201:

        return unit_data, response.status_code

    return None, response.status_code


@pytest.fixture
def create_test_class(client, access_token):

    headers = {
        'Authorization': access_token
    }

    class_data = {
        'class_id': 'btit-sep-2020',
        'class_rep': 'BTIT/574J/2020'
    }

    response = client.post("/api/classes/new",
                           headers=headers, json=class_data)

    if response.status_code == 201:

        return class_data, response.status_code

    return None, response.status_code
