import unittest

import hi


class TestHi(unittest.TestCase):

    def test_hi(self):
        # arrange
        name = "Jack"
        # act
        result = hi.Hi(name)
        # assert
        self.assertEqual("Hi Jack", result)

    def test_hi_2(self):
        # arrange
        name = ""
        # act
        result = hi.Hi(name)
        # assert
        self.assertEqual("Hi World", result)

