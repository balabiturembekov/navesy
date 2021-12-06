from navesy.app import app


def test_root_url():
    """ Test: Корневой url обрабатывается правильно """
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Flask App Run'
