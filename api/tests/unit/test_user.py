from tests.conftest import client


def test_get_users(client):
    response = client.get("/api/users")
    assert response.status_code == 200
