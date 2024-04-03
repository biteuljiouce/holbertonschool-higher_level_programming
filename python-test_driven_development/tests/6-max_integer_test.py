import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_nominal(self):
        self.assertEqual(max_integer([1, 5, 3]), 5)
    def test_empty(self):
        self.assertEqual(max_integer(), None)
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 5]), 5)
    def test_max_at_beginning(self):
        self.assertEqual(max_integer([6, 1, 2, 5]), 6)
    def test_with_one_neg(self):
        self.assertEqual(max_integer([6, -1, 2, 5]), 6)
    def test_with_only_neg(self):
        self.assertEqual(max_integer([-6, -1, -2, -5]), -1)
    def test_only_one(self):
        self.assertEqual(max_integer([666]), 666)
