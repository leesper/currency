from abc import ABC, abstractmethod
class Money(ABC):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency
    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)
    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")
    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")
    @abstractmethod
    def times(self, multiplier):
        pass
    def currency(self):
        return self._currency

class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)
    
class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)