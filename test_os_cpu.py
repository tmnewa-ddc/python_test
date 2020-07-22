import unittest
from unittest import mock

import os_cpu


class TestOSCpu(unittest.TestCase):

    @mock.patch("os.cpu_count")
    def test_cpu(self, mock_os):
        # arrange
        mock_os.return_value = 99999

        # act
        res = os_cpu.os_cpu()

        # assert
        self.assertEqual("cpu count = {}".format(99999), res)

