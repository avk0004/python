class Bank:
    def __init__(self,BankName,Balance):
        self.BName = BankName
        self.bal = Balance 
    def deposit(self,dep):
        self.bal += dep
        return self.bal
    def withdrawal(self,withd):
        self.bal -= withd
        return self.bal
    @classmethod
    def changeName(cls,BankName,balance):
        return cls(BankName,balance)
    @staticmethod
    def Bank_policy(bal):
        if bal>=100:
            print("Bank Polciy")
        else:
            print("balance low")
Name= 'abc'
balance = 5000
bank = Bank(Name,balance)
d= bank.deposit(500)
# Bank Deposit is 500 so 5000+500 = 5500
print(d)
w = bank.withdrawal(100)
# with drawal is 100 so 5500-100 = 5400
print(w)
x = bank.changeName('xyz',4000)
print(x.BName)
b = x.Bank_policy(w)
