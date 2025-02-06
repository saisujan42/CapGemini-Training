import unittest
from  bank_account import BankAccount
class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = BankAccount("John Doe", 100.0)  # Initial balance is 100

    def test_deposit_valid(self):
        self.assertEqual(self.account.deposit(50), 150)  # Balance should be 150

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-20)

    def test_withdraw_valid(self):
        self.assertEqual(self.account.withdraw(30), 70)  # Balance should be 70

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)  # Should raise an error

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

unittest.main()