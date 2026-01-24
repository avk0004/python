from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def verify(self,pins):
        pass
class ATM(Bank):
    def __init__(self,pin):
        self.pin = pin
    def verify(self,pins):
        return pins == self.pin
    def access(self,pins):
        return self.verify(pins)

atm = ATM(1245)
print(atm.access(1254))