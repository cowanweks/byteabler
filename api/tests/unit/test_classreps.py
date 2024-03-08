import pytest
from tests.conftest import client, signin_test_user


@pytest.fixture
def create_test_classrep(client, signin_test_user):

    user_data, access_token, _ = signin_test_user

    assert _ == 200
    assert access_token is not None
    assert user_data is not None

    headers = {
        "Content-Type": "application/json",
        'Authorization': access_token
    }

    classrep_data = {
        "reg_no": "BTIT-574J-2020",
        "class_id": "btit-sep-2020",
        "firstname": "Cowan",
        "middlename": "Kanga",
        "lastname": "Wekesa",
        "email": "cowannwekesa@gmail.com",
        "phoneno": "+254768676944",
    }

    response = client.post("/api/classreps/new",
                           headers=headers, json=classrep_data)

    if response.status_code == 201:

        return classrep_data, access_token, response.status_code

    return None, access_token, response.status_code


def test_create_classrep(client, create_test_classrep):

    classrep_data, access_token, _ = create_test_classrep

    assert _ == 201
    assert classrep_data is not None
    assert access_token is not None


def test_get_classrep(client, create_test_classrep):

    classrep_data, access_token, _ = create_test_classrep

    assert _ == 201
    assert classrep_data is not None
    assert access_token is not None

    classrep_id = classrep_data.get('classrep_id')

    headers = {
        'Authorization': access_token
    }

    response = client.get(f"/api/classreps/{classrep_id}", headers=headers)

    assert response.status_code == 200


def test_get_classreps(client, create_test_classrep):

    classrep_data, access_token, _ = create_test_classrep

    assert _ == 201
    assert classrep_data is not None
    assert access_token is not None

    headers = {
        'Authorization': access_token
    }

    response = client.get("/api/classreps", headers=headers)

    assert response.status_code == 200


def test_update_classrep(client, create_test_classrep):

    classrep_data, access_token, _ = create_test_classrep

    assert _ == 201
    assert classrep_data is not None
    assert access_token is not None

    reg_no = classrep_data.get('reg_no')

    updated_class_rep_data = {
        "reg_no": "BTIT-574J-2020",
        "class_id": "btit-sep-2020",
        "firstname": "Brian",
        "middlename": "Kanga",
        "lastname": "Wekesa",
        "email": "cowannwekesa@gmail.com",
        "phoneno": "+254768676944",
    }

    headers = {
        'Authorization': access_token
    }

    response = client.put(
        f"/api/classreps/edit/{reg_no}", headers=headers, json=updated_class_rep_data)

    assert response.status_code == 201


def test_delete_classrep(client, create_test_classrep):

    classrep_data, access_token, _ = create_test_classrep

    assert _ == 201
    assert classrep_data is not None
    assert access_token is not None

    reg_no = classrep_data.get('reg_no')

    headers = {
        'Authorization': access_token
    }

    response = client.delete(
        f"/api/classreps/delete/{reg_no}", headers=headers)

    assert response.status_code == 200
