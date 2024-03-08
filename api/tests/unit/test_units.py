import pytest
from tests.conftest import client, signin_test_user


@pytest.fixture
def create_test_unit(client, signin_test_user):

    user_data, access_token, _ = signin_test_user

    assert _ == 200
    assert access_token is not None
    assert user_data is not None

    headers = {
        "Content-Type": "application/json",
        'Authorization': access_token
    }

    unit_data = {
        'unit_code': 'UNIT-001',
        'unit_name': 'Human Resources'
    }

    response = client.post("/api/units/new",
                           headers=headers, json=unit_data)

    if response.status_code == 201:

        return unit_data, access_token, response.status_code

    return None, access_token, response.status_code


def test_create_unit(client, create_test_unit):

    unit_data, access_token, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None


def test_get_unit(client, create_test_unit):

    unit_data, access_token, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None

    unit_code = unit_data.get('unit_code')

    headers = {
        'Authorization': access_token
    }

    response = client.get(f"/api/units/{unit_code}", headers=headers)

    assert response.status_code == 200


def test_get_units(client, create_test_unit):

    unit_data, access_token, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None

    headers = {
        'Authorization': access_token
    }

    response = client.get("/api/units", headers=headers)

    assert response.status_code == 200


def test_update_unit(client, create_test_unit):

    unit_data, access_token, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None

    unit_code = unit_data.get('unit_code')

    updated_unit_data = {
        'unit_name': 'Object Oriented Programming'
    }

    headers = {
        'Authorization': access_token
    }

    response = client.put(
        f"/api/units/edit/{unit_code}", headers=headers, json=updated_unit_data)

    assert response.status_code == 201


def test_delete_unit(client, create_test_unit):

    unit_data, access_token, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None

    unit_code = unit_data.get('unit_code')

    headers = {
        'Authorization': access_token
    }

    response = client.delete(f"/api/units/delete/{unit_code}", headers=headers)

    assert response.status_code == 200
