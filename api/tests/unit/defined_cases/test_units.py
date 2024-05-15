from tests.test_data.good_data import new_unit_data, updated_unit_data


def test_create_unit(client):
    headers = {}

    response = client.post(
        "/bytabler/api/v1/units", headers=headers, json=new_unit_data
    )

    assert response.status_code == 201, "{}".format(response.json.get("msg"))


def test_get_unit(client):
    headers = {}

    response = client.get("/bytabler/api/v1/units?unit_id=1", headers=headers)

    assert (response.status_code == 200) or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_get_units(client):
    headers = {}

    response = client.get("/bytabler/api/v1/units", headers=headers)

    assert (response.status_code == 200) or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_update_unit(client):
    headers = {}

    response = client.put(
        "/bytabler/api/v1/units?unit_id=1", headers=headers, json=updated_unit_data
    )

    assert (response.status_code) == 201 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_delete_unit(client):
    headers = {}

    response = client.delete("/bytabler/api/v1/units?unit_id=1", headers=headers)

    assert (response.status_code == 200) or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )
