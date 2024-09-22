import unittest

from Chapter2.multiples import is_number_multiple_of_4
from Chapter2.multiples import is_number_multiple_of_10

class testMultiplesOfNumbers(unittest.TestCase):

    def test_number_multiples(self):
        number = 1024

    def test_number_multiple_of_4(self):
        number = 1024
        output_result = is_number_multiple_of_4(number)
        self.assertEqual(output_result, ["1024 is a multiple of 4"])

    def test_number_multiple_of_4_using_7(self):
        number = 7
        output_result = is_number_multiple_of_4(number)
        self.assertEqual(output_result, ["7 is not a multiple of 4"])

    def test_number_multiple_of_4_using_a_negative_number(self):
        number = -4
        output_result = is_number_multiple_of_4(number)
        self.assertEqual(output_result, ["-4 is a multiple of 4"])

    def test_number_multiple_of_4_using_bigger_figure(self):
        number = 1000000000
        output_result = is_number_multiple_of_4(number)
        self.assertEqual(output_result, ["1000000000 is a multiple of 4"])

    def test_number_multiple_of_10(self):
            number = 2
            output_result = is_number_multiple_of_10(number)
            self.assertEqual(output_result, ["2 is not a multiple of 10"])

    def test_number_multiple_of_10_using_15(self):
        number = 15
        output_result = is_number_multiple_of_10(number)
        self.assertEqual(output_result, ["15 is not a multiple of 10"])

    def test_number_multiple_of_10_using_0_figure(self):
        number = 0
        output_result = is_number_multiple_of_10(number)
        self.assertEqual(output_result, ["0 is a multiple of 10"])

    def test_number_multiple_of_10_using_negative_number(self):
        number = -10
        output_result = is_number_multiple_of_10(number)
        self.assertEqual(output_result, ["-10 is a multiple of 10"])

    def test_number_multiple_of_10_using_a_larger_figure(self):
        number = 1000000000
        output_result = is_number_multiple_of_10(number)
        self.assertEqual(output_result, ["1000000000 is a multiple of 10"])