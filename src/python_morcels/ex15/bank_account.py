# way1
import itertools


class BankAccount:
    """Bank Account with balance, deposit and withdraw operations"""
    _class_counter = itertools.count()
    accounts = []

    def __init__(self, balance: int = 0):
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")
        self._balance = balance

        self._number = next(BankAccount._class_counter)
        BankAccount.accounts.append(self)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    def deposit(self, deposit: int):
        if deposit < 0:
            raise ValueError(f"Cannot deposit {deposit}")

        self._balance += deposit

    def withdraw(self, withdraw: int):
        if withdraw < 0:
            raise ValueError(f"Can't withdraw {withdraw}")

        if self.balance < withdraw:
            raise ValueError(f"Can't withdraw {withdraw} with {self.balance} balance")

        self._balance -= withdraw

    def transfer(self, account, amount: int):
        self.withdraw(amount)
        account.deposit(amount)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(balance={self.balance})"


a1 = BankAccount(100)
a2 = BankAccount()
a3 = BankAccount(50)
assert str(BankAccount.accounts) == "[BankAccount(balance=100), BankAccount(balance=0), BankAccount(balance=50)]"
a1.transfer(a3, 15)
assert str(BankAccount.accounts) == "[BankAccount(balance=85), BankAccount(balance=0), BankAccount(balance=65)]"

a1 = BankAccount()
assert a1.balance == 0

a1.deposit(10)
assert a1.balance == 10

a2 = BankAccount(balance=20)
a2.withdraw(15)
assert a2.balance == 5

a1.transfer(a2, 3)
assert str(a1) == 'BankAccount(balance=7)'
assert str(a2) == 'BankAccount(balance=8)'

try:
    a1 = BankAccount(-10)
except ValueError as e:
    assert str(e) == 'Cannot open account with -10 balance'
else:
    assert False

a1 = BankAccount(balance=10)
try:
    a1.withdraw(-5)
except ValueError as e:
    assert str(e) == "Can't withdraw -5"
else:
    assert False

try:
    a1.withdraw(50)
except ValueError as e:
    assert str(e) == "Can't withdraw 50 with 10 balance"
else:
    assert False

try:
    a1.deposit(-5)
except ValueError as e:
    assert str(e) == "Cannot deposit -5"
else:
    assert False

try:
    a1.transfer(a2, 100)
except ValueError as e:
    assert str(e) == "Can't withdraw 100 with 10 balance"
else:
    assert False

# way2
from dataclasses import dataclass


@dataclass
class BankAccount:
    balance: int = 0

    def __init__(self, balance: int = 0):
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")
        self.balance = balance

    def deposit(self, deposit: int):
        if deposit < 0:
            raise ValueError(f"Cannot deposit {deposit}")
        self.balance += deposit

    def withdraw(self, withdraw: int):
        if withdraw < 0:
            raise ValueError(f"Can't withdraw {withdraw}")
        if self.balance < withdraw:
            raise ValueError(f"Can't withdraw {withdraw} with {self.balance} balance")

        self.balance -= withdraw

    def transfer(self, account, amount: int):
        if self.balance < amount:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")
        self.withdraw(amount)
        account.deposit(amount)


a1 = BankAccount(100)
a2 = BankAccount()
a3 = BankAccount(50)
assert str(BankAccount.accounts) == "[BankAccount(balance=100), BankAccount(balance=0), BankAccount(balance=50)]"
a1.transfer(a3, 15)
assert str(BankAccount.accounts) == "[BankAccount(balance=85), BankAccount(balance=0), BankAccount(balance=65)]"

a1 = BankAccount()
assert a1.balance == 0

a1.deposit(10)
assert a1.balance == 10

a2 = BankAccount(balance=20)
a2.withdraw(15)
assert a2.balance == 5

a1.transfer(a2, 3)
assert str(a1) == 'BankAccount(balance=7)'
assert str(a2) == 'BankAccount(balance=8)'

try:
    a1 = BankAccount(-10)
except ValueError as e:
    assert str(e) == 'Cannot open account with -10 balance'
else:
    assert False

a1 = BankAccount(balance=10)
try:
    a1.withdraw(-5)
except ValueError as e:
    assert str(e) == "Can't withdraw -5"
else:
    assert False

try:
    a1.withdraw(50)
except ValueError as e:
    assert str(e) == "Can't withdraw 50 with 10 balance"
else:
    assert False

try:
    a1.deposit(-5)
except ValueError as e:
    assert str(e) == "Cannot deposit -5"
else:
    assert False

try:
    a1.transfer(a2, 100)
except ValueError as e:
    assert str(e) == "Can't withdraw 100 with 10 balance"
else:
    assert False
