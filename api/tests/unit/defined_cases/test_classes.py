from tests.test_data.good_data import new_class_data, updated_class_data


def test_create_class(client):
    headers = {}
    response = client.post(
        "/api/v1/classes", headers=headers, json=new_class_data
    )

    assert response.status_code == 201, "{}".format(response.json.get("msg"))


def test_get_class(client):
    headers = {}

    response = client.get("/api/v1/classes?class_id=1", headers=headers)

    assert (response.status_code == 200) or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_get_classes(client):
    headers = {}

    response = client.get("/api/v1/classes", headers=headers)

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_update_class(client):
    headers = {}

    response = client.put(
        "/api/v1/classes?class_id=1", headers=headers, json=updated_class_data
    )

    assert response.status_code == 201 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_delete_class(client):
    headers = {}

    response = client.delete("/api/v1/classes?class_id=1", headers=headers)

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )
