import unittest

from Chapter2.arithmetic import  arithmetic_addition_operators
from Chapter2.arithmetic import  arithmetic_subtraction_operators
from Chapter2.arithmetic import  arithmetic_division_operators
from Chapter2.arithmetic import arithmetic_multiplication_operators
from Chapter2.arithmetic import arithmetic_exponentiation_operators
from Chapter2.arithmetic import arithmetic_floor_division_operators

class TestArithmeticOperators(unittest.TestCase):

    def test_for_arithmetic_operators(self):
        right_operand = 2
        left_operand = 27.5


    def test_for_arithmetic_addition_operators(self):
        right_operand = 2
        left_operand = 27.5
        addition = arithmetic_addition_operators(right_operand, left_operand)
        self.assertEqual(addition, 29.5)


    def test_for_arithmetic_subtraction_operators(self):
        right_operand = 2
        left_operand = 27.5
        subtraction = arithmetic_subtraction_operators(right_operand, left_operand)
        self.assertEqual(subtraction, -25.5)


    def test_for_arithmetic_division_operators(self):
        right_operand = 2
        left_operand = 27.5
        division = arithmetic_division_operators(right_operand, left_operand)
        self.assertEqual(division, 0.07272727272727272)


    def test_for_arithmetic_multiplication_operators(self):
        right_operand = 2
        left_operand = 27.5
        multiplication = arithmetic_multiplication_operators(right_operand, left_operand)
        self.assertEqual(multiplication, 55.0)


    def test_for_arithmetic_exponent_operators(self):
        right_operand = 2
        left_operand = 27.5
        exponent = arithmetic_exponentiation_operators(right_operand, left_operand)
        self.assertEqual(exponent, 189812531.24850312)


    def test_for_arithmetic_floor_division_operators(self):
        right_operand = 2
        left_operand = 27.5
        floor_division = arithmetic_floor_division_operators(right_operand, left_operand)
        self.assertEqual(floor_division, 0.0)
