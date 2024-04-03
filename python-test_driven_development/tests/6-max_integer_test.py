import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_nominal(self):
        self.assertEqual(max_integer([1, 5, 3]), 5)
    def test_empty(self):
        self.assertEqual(max_integer(), None)
