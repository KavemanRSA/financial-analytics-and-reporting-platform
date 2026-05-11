'''
A simple budget app that allows users to create categories, deposit and withdraw funds, transfer funds between categories, 
and visualize spending with a simple text-basedbar chart.
The Category class represents a budget category, with methods for managing the ledger and calculating balances.
The create_spend_chart function generates a bar chart showing the percentage of total spending for each category.
'''

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    #Records deposits in the ledger
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    #Records withdrawals in the ledger
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    #Checks balance
    def get_balance(self):
        return sum(record["amount"] for record in self.ledger)

    #Reecords transfers of funds between categories
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    #Checks if funds are available
    def check_funds(self, amount):
        return True if amount <= self.get_balance() else False
