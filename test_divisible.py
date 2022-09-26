import unittest
from divisible import divisible_by


class TestDivisible(unittest.TestCase):
    def test_divisible_by(self):
        test_check_number = 10
        test_divisor = 5
        test_check_number2 = 10
        test_divisor2 = 3
        self.assertTrue(divisible_by(test_check_number,
                        test_divisor), "It's not divisible")
        self.assertFalse(divisible_by(test_check_number2,
                                      test_divisor2), "It's not supposed to be divisible")
