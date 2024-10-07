import unittest

from Chapter2.investment_return import calculate_money_invested


class testInvestmentCalculation(unittest.TestCase):

    def test_calculate_investment(self):
        principal = 1000
        rate = 0.07
        years = 10

    def test_calculate_money_invested_returns_for_ten_years(self):
        principal = 1000
        rate = 0.07
        years = 10
        calculate = calculate_money_invested(principal, rate, years)
        self.assertEqual(calculate, 1967.1513572895665, "After 10 years, the investment will be worth: 1967.15")


    def test_calculate_money_invested_returns_for_twenty_years(self):
        principal = 1000
        rate = 0.07
        years = 20
        calculate = calculate_money_invested(principal, rate, years)
        self.assertEqual(calculate, 3869.6844624861833, "After 20 years, the investment will be worth: 1967.15")


    def test_calculate_money_invested_returns_for_thirty_years(self):
        principal = 1000
        rate = 0.07
        years = 30
        calculate = calculate_money_invested(principal, rate, years)
        self.assertEqual(calculate, 7612.255042662042, "After 30 years, the investment will be worth: 1967.15")


    def test_calculate_money_invested_returns_for_fivety_years(self):
        principal = 1000
        rate = 0.07
        years = 50
        calculate = calculate_money_invested(principal, rate, years)
        self.assertEqual(calculate, 29457.025063071407, "After 50 years, the investment will be worth: 1967.15")

