from fastapi import FastAPI
app = FastAPI()
class Bank:
    def __init__(self, BankName, Balance):
        self.BName = BankName
        self.bal = Balance

    def deposit(self, amount: int):
        self.bal += amount
        return self.bal

    def withdrawal(self, amount: int):
        self.bal -= amount
        return self.bal

    def get_balance(self):
        return self.bal

    def change_name(self, new_name: str):
        self.BName = new_name
        return self.BName

# Create a single bank instance
bank = Bank("ABC", 5000)
@app.get("/")
def home():
    return {"message": "Welcome to the Bank API"}

@app.get("/balance")
def balance():
    return {"balance": bank.get_balance()}

@app.post("/deposit/{amount}")
def deposit(amount: int):
    new_balance = bank.deposit(amount)
    return {"new_balance": new_balance}

@app.post("/withdraw/{amount}")
def withdraw(amount: int):
    new_balance = bank.withdrawal(amount)
    return {"new_balance": new_balance}

@app.post("/change_name/{new_name}")
def change_name(new_name: str):
    updated_name = bank.change_name(new_name)
    return {"bank_name": updated_name}

@app.get("/policy")
def policy():
    if bank.get_balance() >= 100:
        return {"policy": "Bank Policy OK"}
    else:
        return {"policy": "Balance too low"}