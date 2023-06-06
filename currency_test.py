import unittest
from currency import Dollar


class TestCurrency(unittest.TestCase):
    
    # TODO: $5+10CHF = $10 if rate is 2:1
    # $5 * 2 = $10
    # make amount private
    # dollar side effect
    # TODO: money rounding
    # TODO: hashCode
    # TODO: equal null
    # TODO: equal object
    def testMultiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    # equals
    def testEquality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))