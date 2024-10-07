import unittest

from Chapter2.circle_area_diameter_and_circumference import circle_of_diameter
from Chapter2.circle_area_diameter_and_circumference import circle_of_area
from Chapter2.circle_area_diameter_and_circumference import circle_of_circumference


class Test_circle_diameter_and_circumference(unittest.TestCase):

    def test_area_circle(self):
        radius = 2
        pi = 3.14159
        circle_area = circle_of_area(radius, pi)
        self.assertEqual(circle_area, 12.56636)


    def test_circle_diameter(self):
        radius = 2
        circle_diameter = circle_of_diameter(radius)
        self.assertEqual(circle_diameter, 4)


    def test_circle_circumference(self):
        radius = 2
        pi = 3.14159
        circle_circumference = circle_of_circumference(radius, pi)
        self.assertEqual(circle_circumference, 12.56636)
