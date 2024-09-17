import unittest

from Chapter2.From_java_Dietel_to_python.body_mass_Index_calculator import body_mass_calculator


class test_body_mass_index_calculator(unittest.TestCase):

    def test_for_mass_weight(self, weight,height):
        weight = 45
        height = 1.65
        outcome = body_mass_calculator(weight, height)
        self.assertEqual(outcome, "Your are UnderWeight")

    def test_for_normal_weight(self):
        weight = 65
        height = 1.72
        outcome = body_mass_calculator(weight, height)
        self.assertEqual(outcome,"You Have a Normal Weight")

    def test_for_too_much_weight_or_overweight(self):
        weight = 85
        height = 1.75
        outcome = body_mass_calculator(weight, height)
        self.assertEqual(outcome,"You are Getting Overweight")

    def test_for_excess_weight_or_obesity(self):
        weight = 100
        height = 1.75
        outcome = body_mass_calculator(weight, height)
        self.assertEqual(outcome,"You Have Too Much Obesity, You Really need to Work on Yourself")
