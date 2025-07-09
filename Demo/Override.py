class BankAccount:
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if(self.balance - amount < 0):
            raise ValueError("Insufficient balance")

        super().withdraw(amount)

class CurrentAccount(BankAccount):
    pass