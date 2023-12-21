from add_api import app


def test_add_api_no_login():
    # arrange

    # act
    response = app.test_client().get(
        '/add',
        content_type='application/json',
    )

    data = response.json

    # assert
    assert response.status_code == 401


def test_add_api_no_a_b():
    # arrange

    # act
    response = app.test_client().get(
        '/add',
        content_type='application/json',
        query_string={
            'login': 'true'
        }
    )

    data = response.json

    # assert
    assert response.status_code == 400


def test_add_api_no_b():
    # arrange

    # act
    response = app.test_client().get(
        '/add',
        content_type='application/json',
        query_string={
            'login': 'true',
            'a': 1
        }
    )

    data = response.json

    # assert
    assert response.status_code == 400


def test_add_api_no_a():
    # arrange

    # act
    response = app.test_client().get(
        '/add',
        content_type='application/json',
        query_string={
            'login': 'true',
            'b': 2
        }
    )

    data = response.json

    # assert
    assert response.status_code == 400


def test_add_api_ok():
    # arrange

    # act
    response = app.test_client().get(
        '/add',
        content_type='application/json',
        query_string={
            'login': 'true',
            'a': 1,
            'b': 2
        }
    )

    data = response.json

    # assert
    assert response.status_code == 200
    assert data['sum'] == 3

