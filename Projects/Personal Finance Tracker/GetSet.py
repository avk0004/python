from abc import ABC, abstractclassmethod

class ABC:
    @abstractclassmethod
    def Hidden(self,balance):
        pass

class getSet:
    def __init__(self, transaction,types,category):
        self.__transaction = transaction
        self.__types = types
        self.__category = category
    @property
    def Transaction(self):
        return self.__transaction
    @Transaction.setter
    def Transaction(self):
        return self.__transaction
    def Type_Transaction(self,type):
        if type =="Cash":
            class CashTrancation(ABC):
                def __init__(self,amount):
                    self.amount = amount
                def Hidden(self,balance):
                    balance -=self.amount
                    return balance
            return CashTrancation 
                    


    

        