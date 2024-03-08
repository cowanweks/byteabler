import pytest
from tests.conftest import client, signin_test_user


@pytest.fixture
def create_test_role(client, signin_test_user):

    user_data, access_token, _ = signin_test_user

    assert _ == 200
    assert access_token is not None
    assert user_data is not None

    headers = {
        "Content-Type": "application/json",
        'Authorization': access_token
    }

    role_data = {
        'role_id': 'ROLE-001',
        'role_name': 'Administrator'
    }

    response = client.post("/api/roles/new",
                           headers=headers, json=role_data)

    if response.status_code == 201:

        return role_data, access_token, response.status_code

    return None, access_token, response.status_code


def test_create_role(client, create_test_role):

    role_data, access_token, _ = create_test_role

    assert _ == 201
    assert role_data is not None
    assert access_token is not None


def test_get_role(client, create_test_role):

    role_data, access_token, _ = create_test_role

    assert _ == 201
    assert role_data is not None
    assert access_token is not None

    role_id = role_data.get('role_id')

    headers = {
        'Authorization': access_token
    }

    response = client.get(f"/api/roles/{role_id}", headers=headers)

    assert response.status_code == 200


def test_get_roles(client, create_test_role):

    role_data, access_token, _ = create_test_role

    assert _ == 201
    assert role_data is not None
    assert access_token is not None

    headers = {
        'Authorization': access_token
    }

    response = client.get("/api/roles", headers=headers)

    assert response.status_code == 200


def test_update_role(client, create_test_role):

    role_data, access_token, _ = create_test_role

    assert _ == 201
    assert role_data is not None
    assert access_token is not None

    role_id = role_data.get('role_id')

    updated_role_data = {
        'role_name': 'UpdatedRole'
    }

    headers = {
        'Authorization': access_token
    }

    response = client.put(
        f"/api/roles/edit/{role_id}", headers=headers, json=updated_role_data)

    assert response.status_code == 200


def test_delete_role(client, create_test_role):

    role_data, access_token, _ = create_test_role

    assert _ == 201
    assert role_data is not None
    assert access_token is not None

    role_id = role_data.get('role_id')

    headers = {
        'Authorization': access_token
    }

    response = client.delete(f"/api/roles/delete/{role_id}", headers=headers)

    assert response.status_code == 200
