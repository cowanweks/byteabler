from tests.test_data.good_data import new_classrep_data, updated_class_rep_data


def test_create_classrep(client):
    headers = {}

    response = client.post(
        "/api/v1/classreps", headers=headers, json=new_classrep_data
    )

    assert response.status_code == 201, "{}".format(response.json.get("msg"))


def test_get_classrep(client):
    headers = {}

    response = client.get("/api/classreps/1", headers=headers)

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_get_classreps(client):
    headers = {}

    response = client.get("/api/classreps", headers=headers)

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_update_classrep(client):
    headers = {}

    response = client.put(
        "/api/classreps/1", headers=headers, json=updated_class_rep_data
    )

    assert response.status_code == 201 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )


def test_delete_classrep(client):
    headers = {}

    response = client.delete("/api/classreps/1", headers=headers)

    assert response.status_code == 200 or (response.status_code == 404), "{}".format(
        response.json.get("msg")
    )
