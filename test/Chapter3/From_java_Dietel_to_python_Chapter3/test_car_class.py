import unittest

from Chapter3.From_java_Dietel_to_python_Chapter3.car_class import CarClass


class TestMyCarClass(unittest.TestCase):

    def test_setup(self):
        CarClass("Toyota-Corolla", "2015", 1500000.00)

    def test_for_car_model_price_and_year(self):
        car_class = CarClass("Toyota-Corolla", "2015", 1500000.00)
        car_model = "Toyota-Corolla"
        car_year = "2015"
        car_price = 1500000
        self.assertEqual(car_class.get_model(), car_model)
        self.assertEqual(car_class.get_year(), car_year)
        self.assertEqual(car_class.get_price(), car_price)

    def test_for_car_invalid_price(self):
        car_class = CarClass("Toyota-Corolla", "2015", 1500000.00)
        car_price = car_class.set_price(-2500000)
        self.assertEqual(car_class.get_price(), 1500000, car_price)

    def test_for_car_to_validate_year(self):
        car_class = CarClass("Toyota-Corolla", "2015", 1500000.00)
        car_year = car_class.set_year("2023")
        self.assertEqual(car_class.get_year(), "2023", car_year)

    def test_for_car_to_set_and_validate_price(self):
        car_class = CarClass("Range-Rovers", "2015", 1500000.00)
        car_price = car_class.set_price(1500000.00)
        self.assertEqual(car_class.get_price(), 1500000, car_price)

    def test_for_car_to_validate_model(self):
        car_class = CarClass("Range-Rovers", "2015", 1500000.00)
        car_model = car_class.set_model("Bugatti")
        self.assertEqual(car_class.get_model(), "Bugatti", car_model)

    def test_for_car_discount_on_purchase(self):
        car_class = CarClass("Range-Rovers", "2015", 1500000.00)
        car_class.set_model("Ferrari")
        car_class.set_price(6500000.00)
        car_class.set_year("2024")
        car_class.price_discount(7)
        self.assertEqual(car_class.get_price(), 6045000.00)
        car_class.price_discount(5)
        self.assertEqual(car_class.get_price(), 5742750.00)