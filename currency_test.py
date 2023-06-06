import unittest
from currency import Dollar, Franc


class TestCurrency(unittest.TestCase):
    
    # TODO: $5+10CHF = $10 if rate is 2:1
    # $5 * 2 = $10
    # make amount private
    # dollar side effect
    # TODO: money rounding
    # TODO: hashCode
    # TODO: equal null
    # TODO: equal object
    # TODO: Dollar/Franc duplication
    # TODO: Common times
    # TODO: Compare Francs with Dollars
    def testMultiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    # equals
    # Common equals
    def testEquality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))
        self.assertTrue(Franc(5) == Franc(5))
        self.assertFalse(Franc(5) == Franc(6))

    # 5CHF * 2 = 10CHF
    def testFrancMultiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))