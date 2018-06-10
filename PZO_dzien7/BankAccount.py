"""Implementation of the class BankAccount


"""

class BankAccount:
    """"Class BankAccount

    Args:
        balance - the amount of money stored on the account
        """
    def __init__(self, balance):
        if balance <= 0:
            raise ValueError('Balance must be positive.')
        self.balance = balance


    def withdraw(self, amount):
        """"Computes the balance after the withdrawal"""
        if amount <= 0:
            raise ValueError('Amount must be positive.')
        if amount > self.balance:
            raise ValueError('You do not have enough money.')
        return self.balance - amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive.')
        """"Computes the balance after the deposit"""
        return self.balance + amount

bank = BankAccount(100)
print("saldo po wyplacie: ", bank.withdraw(250))
print("saldo po wplacie: ", bank.deposit(50))
