from abc import ABC, abstractmethod

# Abstract class
class Tran(ABC):
    @abstractmethod
    def Hidden(self, balance):
        pass


# Getter / Setter class
class getSet:
    def __init__(self, transaction, types, category):
        self.__transaction = transaction
        self.__types = types
        self.__category = category

    @property
    def Transaction(self):
        return self.__transaction

    @property
    def Types(self):
        return self.__types

    @property
    def Category(self):
        return self.__category
