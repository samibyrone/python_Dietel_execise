import unittest

from Chapter2.From_java_Dietel_to_python.world_population_growth_calculator import estimated_population_growth

class test_world_population_growth_calculator(unittest.TestCase):

    def test_population_after_one_year(self):
        current_population_range = 8.12e9
        growth_rate = 0.0091
        population_estimate = current_population_range * (1 + growth_rate)
        self.assertEqual(population_estimate, estimated_population_growth(current_population_range, growth_rate, 1))

    def test_population_for_zero_growth_rate(self):
        current_population_range = 8.12e9
        growth_rate = 0.00
        population_estimate = current_population_range
        self.assertEqual(population_estimate, estimated_population_growth(current_population_range, growth_rate, 1))

    def test_population_after_two_year(self):
        current_population_range = 8.12e9
        growth_rate = 0.0091
        population_estimate = current_population_range * (1 + growth_rate) ** 2
        self.assertEqual(population_estimate, estimated_population_growth(current_population_range, growth_rate, 2))

    def test_population_after_five_year(self):
        current_population_range = 8.12e9
        growth_rate = 0.0091
        population_estimate = current_population_range * (1 + growth_rate) ** 5
        self.assertEqual(population_estimate, estimated_population_growth(current_population_range, growth_rate, 5))

    def test_population_for_negative_growth_rate(self):
        current_population_range = 8.12e9
        growth_rate = -0.001
        population_estimate = current_population_range * (1 + growth_rate) ** 5
        self.assertEqual(population_estimate, estimated_population_growth(current_population_range, growth_rate, 5))

    def test_large_population_growth_rate_up_to_ten_years(self):
        current_population_range = .1e12
        growth_rate = -0.0091
        population_estimate = current_population_range * (1 + growth_rate) ** 10
        self.assertEqual(population_estimate, estimated_population_growth(current_population_range, growth_rate, 10))