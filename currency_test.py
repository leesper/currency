import unittest
class Dollar:
    def __init__(self, amount):
        self.amount = amount
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
    def __eq__(self, other):
        return self.amount == other.amount

class TestCurrency(unittest.TestCase):
    
    # TODO: $5+10CHF = $10 if rate is 2:1
    # $5 * 2 = $10
    # TODO: make amount private
    # dollar side effect
    # TODO: money rounding
    # TODO: hashCode
    # TODO: equal null
    # TODO: equal object
    def testMultiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEquals(10, product.amount)
        product = five.times(3)
        self.assertEquals(15, product.amount)

    # equals
    def testEquality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))