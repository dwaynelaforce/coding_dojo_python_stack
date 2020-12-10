import random
import datetime

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(interest=0.02, balance=0)]

    def make_deposit(self, amt, acct):
        self.accounts[acct].deposit(amt)

    def make_withdrawal(self, amt, acct):
        self.accounts[acct].withdraw(amt)

    def display_user_balance(self):
        for i in self.accounts:
            self.accounts[i].display_account_info()

    def open_another_acct(self):
        self.accounts.append(BankAccount(interest=0.02, balance=0))


class BankAccount:
    def __init__(self, interest=0.01, balance=0):
        self.acct_num = round(random.random() * 1000000000)
        self.acct_bal = balance
        self.int_rate = interest

    def deposit(self, amt):
        self.acct_bal += amt
        return self
    def withdraw(self, amt):
        self.acct_bal -= amt
        return self
    def display_account_info(self):
        print(f"Account: {self.acct_num} | Balance: {self.acct_bal}")
        return self
    def yield_interest(self):
        self.acct_bal += self.acct_bal * self.int_rate
        return self

dwayne = User("Dwayne LaForce", "dwayne.laforce@gmail.com")
dwayne.open_another_acct()
dwayne.make_deposit(100, 0)
dwayne.make_deposit(3000, 1)
dwayne.display_user_balance()

