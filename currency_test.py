import unittest
from currency import Dollar, Franc, Money

class TestCurrency(unittest.TestCase):
    # $5 * 2 = $10
    # make amount private
    # dollar side effect
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    # equals
    # Common equals
    # Compare Francs to Dollars
    def testEquality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertTrue(Money.franc(5) == Money.franc(5))
        self.assertFalse(Money.franc(5) == Money.franc(6))
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    # 5CHF * 2 = 10CHF
    def testFrancMultiplication(self):
        five = Money.franc(5)
        self.assertEqual(Money.franc(10), five.times(2))
        self.assertEqual(Money.franc(15), five.times(3))

    # Currency
    def testCurrency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    # TODO: $5+10CHF = $10 if rate is 2:1
    # TODO: money rounding
    # TODO: hashCode
    # TODO: equal null
    # TODO: equal object
    # TODO: Dollar/Franc duplication
    # Common times
    def testDifferentClassEquality(self):
        self.assertTrue(Money(10, "CHF") == Franc(10, "CHF"))
    # TODO: delete testFrancMultiplication