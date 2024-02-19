from tests.conftest import client, create_test_unit


def test_get_unit(client, access_token, create_test_unit):

    unit_data, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None

    unit_code = unit_data.get('unit_code')

    headers = {
        'Authorization': access_token
    }

    response = client.get(f"/api/units/{unit_code}", headers=headers)

    assert response.status_code == 200


def test_get_units(client, access_token, create_test_unit):

    unit_data, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None

    headers = {
        'Authorization': access_token
    }

    response = client.get("/api/units", headers=headers)

    assert response.status_code == 200


def test_create_unit(client, access_token, create_test_unit):

    unit_data, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None


def test_update_unit(client, access_token, create_test_unit):

    unit_data, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None

    unit_code = unit_data.get('unit_code')

    updated_unit_data = {
        'unit_name': 'UpdatedRole'
    }

    headers = {
        'Authorization': access_token
    }

    response = client.put(
        f"/api/units/edit/{unit_code}", headers=headers, json=updated_unit_data)

    assert response.status_code == 201


def test_delete_unit(client, access_token, create_test_unit):

    unit_data, _ = create_test_unit

    assert _ == 201
    assert unit_data is not None

    unit_code = unit_data.get('unit_code')

    headers = {
        'Authorization': access_token
    }

    response = client.delete(f"/api/units/delete/{unit_code}", headers=headers)

    assert response.status_code == 200
