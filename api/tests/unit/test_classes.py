import pytest
from tests.conftest import client, signin_test_user


@pytest.fixture
def create_test_class(client, signin_test_user):

    user_data, access_token, _ = signin_test_user

    assert _ == 200
    assert access_token is not None
    assert user_data is not None

    headers = {
        "Content-Type": "application/json",
        'Authorization': access_token
    }

    class_data = {
        'class_id': 'btit-sep-2020',
        'class_rep': 'BTIT/574J/2020'
    }

    response = client.post("/api/classes/new",
                           headers=headers, json=class_data)

    if response.status_code == 201:

        return class_data, access_token, response.status_code

    return None, access_token, response.status_code


def test_create_class(client, create_test_class):

    class_data, access_token, _ = create_test_class

    assert _ == 201
    assert class_data is not None
    assert access_token is not None


def test_get_class(client, create_test_class):

    class_data, access_token, _ = create_test_class

    assert _ == 201
    assert class_data is not None
    assert access_token is not None

    class_id = class_data['class_id']

    headers = {
        'Authorization': access_token
    }

    response = client.get(f"/api/classes/{class_id}", headers=headers)

    assert response.status_code == 200


def test_get_classes(client, create_test_class):

    class_data, access_token, _ = create_test_class

    assert _ == 201
    assert class_data is not None
    assert access_token is not None

    headers = {
        'Authorization': access_token
    }

    response = client.get("/api/classes", headers=headers)

    assert response.status_code == 200


def test_update_class(client, create_test_class):

    class_data, access_token, _ = create_test_class

    assert _ == 201
    assert class_data is not None
    assert access_token is not None

    class_id = class_data.get('class_id')

    updated_class_data = {
        'class_rep': 'BTIT/557J/2020'
    }

    headers = {
        'Authorization': access_token
    }

    print(class_data)

    response = client.put(
        f"/api/classes/edit/{class_id}", headers=headers, json=updated_class_data)

    assert response.status_code == 201


def test_delete_class(client, create_test_class):

    class_data, access_token, _ = create_test_class

    assert _ == 201
    assert class_data is not None
    assert access_token is not None

    class_id = class_data.get('class_id')

    headers = {
        'Authorization': access_token
    }

    response = client.delete(
        f"/api/classes/delete/{class_id}", headers=headers)

    assert response.status_code == 200
