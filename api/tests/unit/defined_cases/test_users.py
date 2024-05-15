from tests.test_data.good_data import (
    new_user_data,
    updated_user_data,
    correct_signin_data,
)


def test_create_user(client):
    headers = {}

    response = client.post(
        "/bytabler/api/v1/users", headers=headers, json=new_user_data
    )

    assert (response.status_code == 201) or (response.status_code == 400), "{}".format(
        response.json.get("msg")
    )


def test_get_users(client):
    headers = {}

    response = client.get("/bytabler/api/v1/users", headers=headers)

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_get_user(client):
    headers = {}

    response = client.get("/bytabler/api/v1/users?user_id=1", headers=headers)

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_update_user(client):
    headers = {}

    response = client.put(
        "/bytabler/api/v1/users?user_id=1",
        headers=headers,
        json=updated_user_data,
    )

    assert response.status_code == 201, "{}".format(response.json.get("msg"))


def test_delete_user(client):
    """ """

    headers = {}

    response = client.delete("/bytabler/api/v1/users?user_id=1", headers=headers)

    assert (response.status_code == 200) or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_signin_user(client):
    """ """

    headers = {}

    response = client.post(
        "/bytabler/api/v1/signin", headers=headers, json=correct_signin_data
    )

    assert response.status_code == 200 or (response.status_code == 401), "{}".format(
        response.json.get("msg")
    )


def test_signout_user(client):
    """ """

    headers = {}

    username = correct_signin_data.get("username")

    response = client.get(
        f"/bytabler/api/v1/signout?username={username}", headers=headers
    )

    assert response.status_code == 200, "{}".format(response.json.get("msg"))
