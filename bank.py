class Customer:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __eq__(self, other):
        return self.firstName == other.firstName and self.lastName == other.lastName

import datetime
class Transaction:

    def __init__(self, amount, date=datetime.datetime.now()):
        self.amount = amount
        self.date = date

from typing import List
class BankAccount:

    nb = 0

    def __init__(self, owner:Customer):
        self.owner = owner
        self._balance = 0
        BankAccount.nb += 1
        self.transactions:List[Transaction] = []

    def __del__(self):
        BankAccount.nb -= 1

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(-amount))
            return amount
        else:
            raise ValueError("Amount > balance")

    def __eq__(self, other):
        return self.owner == other.owner and self.balance == other.balance

    def __ne__(self, other):
        return not self.__eq__(other)

    def __cmp__(self, other):
        return self.balance - other.balance

import unittest
class BankTest(unittest.TestCase):

    def testDirty(self):
        ba = BankAccount(Customer("Cyril","Vincent"))
        ba.toto = "titi"
        self.assertEqual("titi", ba.toto)

    def testAccount(self):
        ba = BankAccount("Cyril")
        self.assertEqual(0, ba.balance)
        ba.deposit(100)
        self.assertEqual(100, ba.balance)
        amount = ba.withdraw(70)
        self.assertEqual(70, amount)
        self.assertEqual(30, ba.balance)
        BankAccount.deposit(ba, 100)
        print(ba.__dict__)
        ba.__dict__["balance"] += 100
        ba.__dict__ = {'owner': 'Cyril', 'balance': 130}
        ba._balance += 100


    def testEqualVsIs(self):
        l1 = [1,2]
        l2 = [1,2]
        self.assertTrue(l1 == l2)
        self.assertFalse(l1 is l2)

        ba1 = BankAccount(Customer("Cyril","Vincent"))
        ba2 = BankAccount(Customer("Cyril","Vincent"))
        self.assertTrue(ba1 == ba2)
        self.assertFalse(ba1 is ba2)

    def testStatic(self):
        ba1 = BankAccount("toto")
        ba2 = BankAccount("titi")
        self.assertEqual(2, BankAccount.nb)
        del(ba1)
        self.assertEqual(1, BankAccount.nb)



