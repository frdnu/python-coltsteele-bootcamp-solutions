# base class and encapsulation

"""
Design a class BankAccount that encapsulates financial account data defensively:
Class Attribute: Set a class-level string bank_name = "Apex Financial Services".
Constructor (__init__): Accept owner (str) and an optional balance (float, default 0.0). Store balance inside a protected variable _balance.
Property Read-Only Getter: Implement a @property decorator for balance that returns _balance as a float. Do not provide a setter (making balance read-only to external assignments).
Instance Methods:
deposit(amount: float) -> float: Validates that amount > 0. If valid, adds to _balance and logs the transaction. If invalid, raises a ValueError("Deposit amount must be strictly positive.").
withdraw(amount: float) -> float: Validates that amount > 0 and amount <= _balance. If valid, subtracts from _balance. Otherwise, raises a ValueError("Insufficient funds for transaction execution.").
"""


class BankAccount:

    bank_name = "Apex Financial Services"

    def __init__(self, owner: str, balance=0.0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            raise ValueError("Deposit amount must be strictly positive.")

    def withraw(self, amount: float) -> float:
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            raise ValueError("Insufficient funds for transaction execution.")
