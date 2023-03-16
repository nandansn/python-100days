import random

class BankAccount:
    def __init__(self, amount):
        self.amount = amount
        self.account_number = random.randint(1000,2000)
        print("object created")

    def balance(self):
        return {"amount":self.amount,
        "account_number":self.account_number}

    def deposit(self, amt):

        self.amount += amt
        print(f"amount deposited {amt}, balance amount is {self.balance()}")

    def withdraw(self, amt):

        if amt > self.amount:
            print(f"balance is {self.balance()} less than than amount to be withdrawn {amt}")
        else:
            self.amount -= amt
            print(f"amount {amt} withdrawn, balance amount is {self.balance()}")

        



nanda = BankAccount(1000)

print(nanda.balance())
nanda.deposit(10000)
nanda.withdraw(3000)
nanda.withdraw(10000)

