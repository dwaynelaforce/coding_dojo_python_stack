# Assignment: User
# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

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

lourdes = User("Lourdes Rodriguez")
esteban = User()
dwayne = User("Dwayne LaForce")

lourdes.deposit(1261).deposit(516).deposit(47).withdrawal(333)
esteban.deposit(256).deposit(150).withdrawal(15).withdrawal(65)
dwayne.deposit(999).withdrawal(50).withdrawal(20).withdrawal(1000)
lourdes.transfer_to(500, dwayne)
