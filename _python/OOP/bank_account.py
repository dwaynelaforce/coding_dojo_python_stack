import random
import datetime

class User:
    def __init__(self, name="unknown"):
        self.acct_holder_name = name
        self.acct_num = round(random.random() * 1000000000)
        self.acct_bal = 0.00
        self.acct_history = []
        print("Account has been opened")
        self.print_act_info()

    def print_act_info(self):
        print("Account information:")
        print(f"User: {self.acct_holder_name}")
        print(f"Account No: {self.acct_num}")
        print(f"Balance: ${self.acct_bal}\n")
        self.print_acct_hist()

    def print_acct_hist(self):
        print(f"Account history for {self.acct_holder_name}, account number {self.acct_num}:")
        if len(self.acct_history) < 1:
            print("No history to display")
        for i in self.acct_history:
            print(i)
        print("\n")

    def update_hist(self, type, amt):
        self.acct_history.append([type, "$"+str(amt), datetime.date.today()])

    def withdrawal(self, amt):
        self.acct_bal -= amt
        self.update_hist("Withdrawal", amt)
        print(f"Your withdrawal of ${amt} has been processed.")
        self.print_act_info()
        return self

    def deposit(self, amt):
        self.acct_bal += amt
        self.update_hist("Deposit", amt)
        print(f"Your deposit of ${amt} has been processed.")
        self.print_act_info()
        return self

    def transfer_to(self, amt, person):
        self.withdrawal(amt)
        person.deposit(amt)
        print(f"Transfer ${amt} to account holder: {person.acct_holder_name}, account {person.acct_num}")
        self.print_act_info()
        return self

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

# savings1 = BankAccount(0.02, 100)
# savings2 = BankAccount(0.05, 999)

# savings1.deposit(15).deposit(20).deposit(25).withdraw(5).yield_interest().display_account_info()
# savings2.deposit(42069).deposit(666).withdraw(300).withdraw(3).withdraw(2.50).withdraw(50).yield_interest().display_account_info()

dwayne = User("Dwayne LaForce")
monica = User("Monica Hong")
dwayne.deposit(500).deposit(300).withdraw(700).transfer_to(50, monica)