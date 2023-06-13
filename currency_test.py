import unittest
from currency import Money, Bank, Sum

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
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    # Currency
    def testCurrency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())
    
    # TODO: $5+10CHF = $10 if rate is 2:1
    # TODO: $5 + $5 = $10
    # TODO: return Money from $5 + $5
    # TODO: reduce Money with conversion
    # TODO: reduce(Bank, String)
    # Bank.reduce(Money)
    def testReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)
    def testPlusReturnsSum(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)
    def testReduceSum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(7), result)
    def testSimpleAddtion(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(10), reduced)
    # TODO: money rounding
    # TODO: hashCode
    # TODO: equal null
    # TODO: equal object
    # TODO: Dollar/Franc duplication
    # TODO: delete testFrancMultiplication