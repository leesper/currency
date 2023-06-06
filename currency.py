from abc import ABC, abstractmethod
class Money(ABC):
    def __init__(self, amount=0):
        self._amount = amount
    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)
    @staticmethod
    def dollar(amount):
        return Dollar(amount)
    @staticmethod
    def franc(amount):
        return Franc(amount)
    @abstractmethod
    def times(self, multiplier):
        pass

class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)
    
class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)
    def times(self, multiplier):
        return Franc(self._amount * multiplier)