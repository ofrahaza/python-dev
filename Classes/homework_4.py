import math
import random


class Account:
    def __init__(self, account_number: int, customer_name: str, customer_address: str,
                 initial_balance: float = 0):  #
        self.balance = initial_balance
        self.customer_name = customer_name
        self.account_number = account_number
        self.customer_address = customer_address

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def __repr__(self):
        print(
            f"Account {self.account_number} by {self.customer_name} ({self.customer_address}), balance {self.balance}")  # добавили функцию __repr__ для класса Account


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer_name: str, customer_address: str,
                       initial_balance: float = 0) -> Account:
        account_number = _generate_account_number()
        account = Account(account_number, customer_name, customer_address, initial_balance)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number: int) -> Account:
        if account_number in self.accounts.keys():
            return self.accounts[account_number]
        else:
            raise ValueError("Account not found")


def _generate_account_number() -> int:
    return math.floor(random.random() * 1000000)


class Customer:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address


def banking_scenario():
    bank = Bank()
    customer1 = Customer("Alice", "Moscow, Stremyannyi per, 1")
    customer2 = Customer("Bob", "Vorkuta, ul. Lenina, 5")

    # Alice opens an account and deposits some money
    alice_account = bank.create_account(customer1.name, customer1.address, initial_balance=500.0)
    alice_account.deposit(100.0)
    print(f"Alice's balance: {alice_account.balance}")  # Alice's balance: 600.0

    # Bob opens an account and deposits some money
    bob_account = bank.create_account(customer2.name, customer2.address, initial_balance=1000.0)
    bob_account.deposit(500.0)
    print(f"Bob's balance: {bob_account.balance}")  # Bob's balance: 1500.0

    # Alice withdraws some money from her account
    alice_account.withdraw(300.0)
    print(f"Alice's balance: {alice_account.balance}")  # Alice's balance: 300.0

    # Alice tries to withdraw more money than she has in her account
    try:
        alice_account.withdraw(500.0)
    except ValueError as e:
        print(e)  # Insufficient funds

    # Bank retrieves Alice's account using the account number
    retrieved_account = bank.get_account(alice_account.account_number)
    alice_account.__repr__()

banking_scenario()