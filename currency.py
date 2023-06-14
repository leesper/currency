from abc import ABC, abstractmethod
class Expression(ABC):
    def reduce(self, bank, to):
        pass
    def plus(self, addend):
        pass

class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency
    def __eq__(self, other):
        return self._amount == other._amount \
            and self.currency() == other.currency()
    def __str__(self):
        return f'{self._amount} {self._currency}'
    def __repr__(self):
        return f'{self._amount} {self._currency}'
    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")
    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")
    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)
    def currency(self):
        return self._currency
    def plus(self, addend):
        return Sum(self, addend)
    def reduce(self, bank, to):
        rate = bank.rate(self.currency(), to)
        return Money(self._amount / rate, to)

class Bank:
    def __init__(self):
        self.__rates = dict()
    def reduce(self, source, to):
        return source.reduce(self, to)
    def rate(self, frm, to):
        if frm == to:
            return 1
        return self.__rates[Pair(frm, to)]
    def addRate(self, frm, to, rate):
        self.__rates[Pair(frm, to)] = rate
    
class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend
    def reduce(self, bank, to):
        amount = self.augend.reduce(bank, to)._amount \
            + self.addend.reduce(bank, to)._amount
        return Money(amount, to)
    def plus(self, addend):
        return Sum(self, addend)
    
class Pair:
    def __init__(self, frm, to):
        self.__frm = frm
        self.__to = to
    def __eq__(self, other):
        return self.__frm == other.__frm and self.__to == other.__to
    def __hash__(self):
        return hash((self.__frm, self.__to))