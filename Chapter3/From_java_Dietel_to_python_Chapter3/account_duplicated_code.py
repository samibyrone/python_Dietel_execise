from decimal import Decimal

class Account:

    def __init__(self, name: str, balance = Decimal(0.00)):
        self.name = name
        self.balance = balance

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_balance(self, balance):
        if balance > 0.0: self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0.0: self.balance += amount
        else: print("Invalid Deposit Amount!!!, You Don't Have Enough Money Biko")

    def withdraw(self, amount):
        self.balance -= amount


def display_account(accounts):
    print(accounts)

def deposit_for_account(accounts):
    accounts.set_name = str(input("\nWhat is your full name? "))
    accounts.deposit = float(input("\nHow much money would you like to deposit for? "))

    print(f"\nYou Deposited {accounts.deposit:.2f} into the Account of{accounts.get_name()}")

    display_account(accounts)