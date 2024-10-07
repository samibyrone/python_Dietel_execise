import unittest

from Chapter3.From_java_Dietel_to_python_Chapter3.account_duplicated_code import Account

class TestAccountDuplicatedCode(unittest.TestCase):

    def test_account_setup(self):
        account = Account("Samibyrone", 100.0)

    def test_to_initiate_account_with_balance(self):
        account = Account("Samibyrone olarewaju", 100.0)
        name = "Samibyrone olarewaju"
        self.assertAlmostEqual(account.get_name(), name)
        balance = 100.00
        self.assertAlmostEqual(account.get_balance(), balance)
        self.assertEqual(Account("Samibyrone", balance).get_balance(), balance)

    def test_to_initiate_account_and_validate_account_with_account_name(self):
        account = Account("Samibyrone", 100.0)
        name = "Samibyrone"
        self.assertAlmostEqual(account.get_name(), name)
        name = account.set_name("Adegoke Benjamin")
        self.assertAlmostEqual(account.set_name("Adegoke Benjamin"), name)

    def test_to_initiate_account_and_validate_account_with_account_balance(self):
        account = Account("Samibyrone", 100.0)
        balance = 100.00
        self.assertAlmostEqual(account.get_balance(), balance)
        balance = account.set_balance(1500.00)
        self.assertAlmostEqual(account.set_balance(1500.00), balance)

    def test_to_deposit_into_account_with_new_available_balance(self):
        account = Account("Samibyrone", 100.0)
        account.set_balance(100.00)
        deposit = account.deposit(4500.0)
        self.assertEqual(account.get_balance(), 4600.00, deposit)

    def test_to_deposit_negative_amount_into_account_with_balance(self):
        account = Account("Samibyrone", 100.0)
        account.set_balance(100.0)
        deposit = account.deposit(-4500.0)
        self.assertEqual(account.get_balance(), 100.0, deposit)