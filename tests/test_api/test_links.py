from http import HTTPStatus


def test_create_link(client):
    response = client.post('/v1/links', json={'origin': 'https://example.com'})

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'origin': 'https://example.com',
        'short': 'http://localhost:8000/1',
    }
