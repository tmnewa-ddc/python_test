import unittest
from unittest.mock import patch

import class_cpu


class TestClassCpu(unittest.TestCase):

    @patch.object(class_cpu.CpuInfo, 'cpu_count')
    def test_hi(self, mock_cpu_count):
        # arrange
        mock_cpu_count.return_value = 66666

        # act
        res = class_cpu.say_cpu_count()
        # assert
        mock_cpu_count.assert_called_once()
        self.assertEqual(66666, res)
