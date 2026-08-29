import unittest
from divide import divide
class TestDivide(unittest.TestCase):
    def test_normal_division(self):
        self.assertEqual(
            divide(10,2),
            5
        )
    def test_decimal_result(self):
        self.assertEqual(
            divide(5,2),
            2.5
        )
    def test_negative_number(self):
        self.assertEqual(
            divide(10,-2),
            -5
        )
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10,0)