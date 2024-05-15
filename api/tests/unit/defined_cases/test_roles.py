from tests.test_data.good_data import new_role_data, updated_role_data


def test_create_role(client):
    headers = {
        "Content-Type": "application/json",
    }

    response = client.post(
        "/bytabler/api/v1/roles", headers=headers, json=new_role_data
    )

    assert response.status_code == 201, "{}".format(response.json.get("msg"))


def test_get_role(client):
    headers = {}

    response = client.get("/bytabler/api/v1/roles?role_id=1", headers=headers)

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_get_roles(client):
    headers = {}

    response = client.get("/bytabler/api/v1/roles", headers=headers)

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_update_role(client):
    headers = {}

    response = client.put(
        "/bytabler/api/v1/roles?role_id=1", headers=headers, json=updated_role_data
    )

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_delete_role(client):
    headers = {}

    response = client.delete("/bytabler/api/v1/roles?role_id=1", headers=headers)

    assert (response.status_code == 200) or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )
