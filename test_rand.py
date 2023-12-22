from pytest_mock import MockerFixture
import rand
import numpy as np


def test_rand(mocker: MockerFixture):
    # arrange
    l = [1, 2, 3]
    mock_choice = mocker.patch("random.choice")
    mock_choice.return_value = 2

    # act
    result = rand.rand(l)

    # assert
    mock_choice.assert_called_once_with(l)
    assert result == 2


def test_lucky_is_false(mocker: MockerFixture):
    # arrange

    mock_choice = mocker.patch("random.choice")
    mock_choice.return_value = 500
    array = list(np.arange(1, 1000000 + 1))

    # act
    result = rand.lucky()

    # assert
    mock_choice.assert_called_once_with(array)
    assert result is False


def test_lucky_is_true(mocker: MockerFixture):
    # arrange

    mock_choice = mocker.patch("random.choice")
    mock_choice.return_value = 1
    array = list(np.arange(1, 1000000 + 1))

    # act
    result = rand.lucky()

    # assert
    mock_choice.assert_called_once_with(array)
    assert result is True
