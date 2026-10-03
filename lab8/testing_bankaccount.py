import unittest

from bankaccount import BankAccount

class testBankaccount(unittest.TestCase):
    def setUp(self):
        self.a1 = BankAccount("Evan Dong", 10000)

    def test_balance(self):
        self.assertEqual(self.a1.balance, 10000)

    def test_deposit(self):
        self.a1.deposit(5000)
        self.a1.deposit(10000)
        self.a1.deposit(2500)
        self.assertEqual(self.a1.balance, 27500)

    def test_withdrawl(self):
            self.a1.withdraw(5000)
            self.a1.withdraw(2500)
            self.a1.withdraw(1000)
            self.assertEqual(self.a1.balance, 1500)

    # def test_withdrawlError(self):
             # self.a1.withdraw(15000)
             # self.assertIsNone(self.a1.balance)
            # remove this comment and the hastags above it

if __name__ == "__main__":
    unittest.main()