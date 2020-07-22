import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("teardown")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @unittest.expectedFailure
    def test_split_2(self):
        self.assertEqual(1, 2, "good")

    @unittest.skip("demonstrating skipping")
    def test_skip(self):
        self.fail("test fail")

    @unittest.skipIf(True, "skip if = true")
    def test_skip2(self):
        self.fail("test fail 2")
