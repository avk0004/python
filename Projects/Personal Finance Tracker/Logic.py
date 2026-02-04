from GetSet import getSet, Tran

Getset = getSet("Online", "Cash", "Fitness")


class CashTransaction(Tran):
    def __init__(self, amount):
        self.amount = amount

    def Hidden(self, balance):
        return balance - self.amount

    def Type_Transaction(self, balance):
        if Getset.Types == "Cash":
            return self.Hidden(balance)
        return balance


# Main execution
amount = int(input("Enter cash amount: "))
Transaction = CashTransaction(amount)
m = Transaction.Type_Transaction(20000)
print(m)
