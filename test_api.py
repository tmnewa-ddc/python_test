from flask import json
from pytest_mock import MockFixture

from api import app


def test_cpu_api(mocker: MockFixture):
    # arrange
    expect_cpus = 99999

    mock_cpu_count = mocker.patch("os.cpu_count")
    mock_cpu_count.return_value = expect_cpus

    # act
    response = app.test_client().get(
        '/cpu',
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))

    # assert
    mock_cpu_count.assert_called_once()
    assert expect_cpus == data['cpus']

