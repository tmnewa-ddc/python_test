from pytest_mock import MockerFixture
import cpu


def test_cpu():
    # arrange

    # act
    s = cpu.cpu_count()

    # assert
    assert s == 12


def test_cpu_mock(mocker: MockerFixture):
    # arrange

    mock_cpu_count = mocker.patch("os.cpu_count")
    mock_cpu_count.return_value = 99999

    # act
    s = cpu.cpu_count()

    # assert
    mock_cpu_count.assert_called_once()
    assert s == 99999
