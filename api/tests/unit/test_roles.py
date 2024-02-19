from tests.conftest import client, create_test_role


def test_get_role(client, access_token, create_test_role):

    role_data, _ = create_test_role

    assert _ == 201
    assert role_data is not None

    role_id = role_data.get('role_id')

    headers = {
        'Authorization': access_token
    }

    response = client.get(f"/api/roles/{role_id}", headers=headers)

    assert response.status_code == 200


def test_get_roles(client, access_token, create_test_role):

    role_data, _ = create_test_role

    assert _ == 201
    assert role_data is not None

    headers = {
        'Authorization': access_token
    }

    response = client.get("/api/roles", headers=headers)

    assert response.status_code == 200


def test_create_role(client, access_token, create_test_role):

    role_data, _ = create_test_role

    assert _ == 201
    assert role_data is not None


def test_update_role(client, access_token, create_test_role):

    role_data, _ = create_test_role

    assert _ == 201
    assert role_data is not None

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


def test_delete_role(client, access_token, create_test_role):

    role_data, _ = create_test_role

    assert _ == 201
    assert role_data is not None

    role_id = role_data.get('role_id')

    headers = {
        'Authorization': access_token
    }

    response = client.delete(f"/api/roles/delete/{role_id}", headers=headers)

    assert response.status_code == 200
