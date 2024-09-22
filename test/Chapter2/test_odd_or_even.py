import unittest

from Chapter2.odd_or_even import is_number_even

class testEvenOrOddNumbers(unittest.TestCase):

    def test_that_number_is_even(self):
        number = 10
        output = is_number_even(number)
        self.assertEqual(output, True)
        self.assertEqual(is_number_even(200), True)

    def test_that_number_is_not_even(self):
        number = 15
        output = is_number_even(number)
        self.assertEqual(output, False)
        self.assertEqual(is_number_even(175), False)
