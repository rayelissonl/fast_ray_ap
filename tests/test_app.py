from http import HTTPStatus

# @pytest.fixture()
# def client():
# return TestClient(app)


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


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testray',
                'email': 'testray@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testray',
            'password': '123',
            'email': 'testray@examrle.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'testray',
        'email': 'testray@examrle.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
