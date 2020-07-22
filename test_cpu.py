import unittest
from unittest import mock

import cpu


class TestInfo(unittest.TestCase):

    def test_cpu(self):
        # arrange

        # act
        s = cpu.get_cpu()

        # assert
        self.assertEqual("cpu count = 12", s)

    @mock.patch('cpu.cpu_count')
    def test_cpu_mock(self, mock_cpu_count):
        # arrange
        mock_cpu_count.return_value = 99999

        # act
        s = cpu.get_cpu()

        # assert
        mock_cpu_count.assert_called_once()
        self.assertEqual("cpu count = 99999", s)
