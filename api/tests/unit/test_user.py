from tests.conftest import client, signin_test_user, create_test_user


def test_create_user(client, create_test_user):

    user_data, _ = create_test_user

    assert _ == 201
    assert user_data is not None


def test_get_user(client, signin_test_user):

    user_data, access_token, _ = signin_test_user

    assert _ == 200
    assert user_data is not None
    assert access_token is not None

    username = user_data.get('username')

    headers = {
        'Authorization': access_token
    }

    response = client.get(
        f"/api/users/{username}", headers=headers)

    assert response.status_code == 200


def test_get_users(client, signin_test_user):

    user_data, access_token, _ = signin_test_user

    assert _ == 200
    assert user_data is not None
    assert access_token is not None

    headers = {
        'Authorization': access_token
    }

    response = client.get("/api/users", headers=headers)

    assert response.status_code == 200


def test_update_user(client, signin_test_user):

    user_data, access_token, _ = signin_test_user

    assert _ == 200
    assert user_data is not None
    assert access_token is not None

    username = user_data.get('username')

    updated_data = {
        'role_id': 'Lecturer',
        'username': 'newuser',
        'password': 'cowanweks',
        'confirm_password': 'cowanweks',
        'email': 'newuser@example.com'
    }

    headers = {
        'Authorization': access_token
    }

    response = client.put(f"/api/users/edit/{username}",
                          headers=headers, json=updated_data)

    assert response.status_code == 201


def test_delete_user(client, signin_test_user):

    user_data, access_token, _ = signin_test_user

    assert _ == 200
    assert user_data is not None
    assert access_token is not None

    username = user_data['username']

    headers = {
        'Authorization': access_token
    }

    response = client.delete(f"/api/users/delete/{username}", headers=headers)

    assert response.status_code == 200
