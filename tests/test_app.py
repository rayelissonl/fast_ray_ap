from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_ray_ap.app import app


@pytest.fixture()
def client():
    return TestClient(app)


def test_read_root_deve_retornar_ola_mundo(client):
    # client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'messsage': 'Ola Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testray',
            'email': 'testray@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testray',
        'email': 'testray@example.com',
        'id': 1,
    }
