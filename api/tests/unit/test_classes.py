from tests.conftest import client, create_test_class


def test_get_class(client, access_token, create_test_class):

    class_data, _ = create_test_class

    assert _ == 201
    assert class_data is not None

    class_id = class_data['class_id']

    headers = {
        'Authorization': access_token
    }

    response = client.get(f"/api/classes/{class_id}", headers=headers)

    assert response.status_code == 200


def test_get_classes(client, access_token, create_test_class):

    class_data, _ = create_test_class

    assert _ == 201
    assert class_data is not None

    headers = {
        'Authorization': access_token
    }

    response = client.get("/api/classes", headers=headers)

    assert response.status_code == 200


def test_create_class(client, access_token, create_test_class):

    class_data, _ = create_test_class

    assert _ == 201
    assert class_data is not None


def test_update_class(client, access_token, create_test_class):

    class_data, _ = create_test_class

    assert _ == 201
    assert class_data is not None

    class_id = class_data.get('class_id')

    updated_class_data = {
        'class_rep': 'BTIT/557J/2020'
    }

    headers = {
        'Authorization': access_token
    }

    print(class_data)

    response = client.put(
        f"/api/classes/edit/{class_id}", headers=headers, json=updated_class_data)

    assert response.status_code == 201


def test_delete_class(client, access_token, create_test_class):

    class_data, _ = create_test_class

    assert _ == 201
    assert class_data is not None

    class_id = class_data.get('class_id')

    headers = {
        'Authorization': access_token
    }

    response = client.delete(
        f"/api/classes/delete/{class_id}", headers=headers)

    assert response.status_code == 200
