import unittest

from Chapter3.From_java_Dietel_to_python_Chapter3.petrol_purchase import PetrolPurchase

class TestPetrolPurchase(unittest. TestCase):

    def test_setup(self):
        PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)

    def test_for_petrol_purchase(self):
        purchase = PetrolPurchase("Abuja", "Black-Market", 200, 1200, 0.10)
        location = "Abuja"
        petrol_type = "Black-Market"
        quantity = 200
        price = 1200
        discount = 0.10
        self.assertEqual(purchase.get_location(), location)
        self.assertEqual(purchase.get_petrol_type(), petrol_type)
        self.assertEqual(purchase.get_quantity(), quantity)
        self.assertEqual(purchase.get_price(), price)
        self.assertEqual(purchase.get_price_discount(), discount)

    def test_the_location_for_petrol_purchase(self):
        purchase = PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)
        location = purchase.set_location("Abuja")
        self.assertEqual(purchase.set_location("Abuja"), location)
        purchase.get_location()
        self.assertEqual(purchase.get_location(), "Abuja")

    def test_the_type_of_petrol_purchase_on_location(self):
        purchase = PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)
        location = purchase.set_location("Abuja")
        petrol_type = purchase.set_petrol_type("Regular")
        self.assertEqual(purchase.set_location("Abuja"), location)
        self.assertEqual(purchase.set_petrol_type("Regular"), petrol_type)
        purchase.get_location()
        purchase.get_petrol_type()
        self.assertEqual(purchase.get_location(), "Abuja")
        self.assertEqual(purchase.get_petrol_type(), "Regular")

    def test_for_the_quantity_of_petrol_purchase_on_location(self):
        purchase = PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)
        location = purchase.set_location("Abeokuta")
        petrol_type = purchase.set_petrol_type("Regular")
        quantity = purchase.set_quantity(750)
        self.assertEqual(purchase.set_location("Abeokuta"), location)
        self.assertEqual(purchase.set_petrol_type("Regular"), petrol_type)
        self.assertEqual(purchase.set_quantity(750), quantity)
        purchase.get_location()
        purchase.get_petrol_type()
        purchase.get_quantity()
        self.assertEqual(purchase.get_location(), "Abeokuta")
        self.assertEqual(purchase.get_petrol_type(), "Regular")
        self.assertEqual(purchase.get_quantity(), 750)

    def test_for_the_price_of_petrol_purchase_on_location(self):
        purchase = PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)
        location = purchase.set_location("ogun-state")
        petrol_type = purchase.set_petrol_type("Regular")
        quantity = purchase.set_quantity(450)
        price = purchase.set_price(850)
        self.assertEqual(purchase.set_location("ogun-state"), location)
        self.assertEqual(purchase.set_petrol_type("Regular"), petrol_type)
        self.assertEqual(purchase.set_quantity(450), quantity)
        self.assertEqual(purchase.set_price(850), price)
        purchase.get_location()
        purchase.get_petrol_type()
        purchase.get_quantity()
        purchase.get_price()
        self.assertEqual(purchase.get_location(), "ogun-state")
        self.assertEqual(purchase.get_petrol_type(), "Regular")
        self.assertEqual(purchase.get_quantity(), 450)
        self.assertEqual(purchase.get_price(), 850)

    def test_for_the_discount_from_petrol_purchase_on_location(self):
        purchase = PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)
        location = purchase.set_location("river-state")
        petrol_type = purchase.set_petrol_type("Regular")
        quantity = purchase.set_quantity(850)
        price = purchase.set_price(750)
        discount = purchase.set_price_discount(0.10)
        self.assertEqual(purchase.set_location("river-state"), location)
        self.assertEqual(purchase.set_petrol_type("Regular"), petrol_type)
        self.assertEqual(purchase.set_quantity(850), quantity)
        self.assertEqual(purchase.set_price(750), price)
        self.assertEqual(purchase.set_price_discount(0.10), discount)
        purchase.get_location()
        purchase.get_petrol_type()
        purchase.get_quantity()
        purchase.get_price()
        purchase.get_price_discount()
        self.assertEqual(purchase.get_location(), "river-state")
        self.assertEqual(purchase.get_petrol_type(), "Regular")
        self.assertEqual(purchase.get_quantity(), 850)
        self.assertEqual(purchase.get_price(), 750)
        self.assertEqual(purchase.get_price_discount(), 0.10)

    def test_to_calculate_petrol_purchase_amount(self):
        purchase = PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)
        purchase.get_price_discount()
        amount = 500 * 1000 * (1 - 0.08 / 100)
        self.assertAlmostEqual(purchase.get_purchase_price(), amount)

    def test_to_calculate_zero_discount_on_each_petrol_purchase(self):
        purchase = PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)
        purchase.set_price_discount(0.00)
        purchase.get_price_discount()
        amount = 500 * 1000 * (1 - 0.00 / 100)
        self.assertAlmostEqual(purchase.get_purchase_price(), amount)

    def test_to_calculate_negative_discount_amount_on_petrol_purchase(self):
        purchase = PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)
        purchase.set_price_discount(-0.20)
        purchase.get_price_discount()
        amount = 500 * 1000 * (1 - (-0.20 / 100))
        self.assertEqual(purchase.get_purchase_price(), amount)

    def test_to_check_for_negative_price_on_each_petrol_purchase(self):
        purchase = PetrolPurchase("Lagos", "Filling-station", 500, 1000, 0.08)
        purchase.set_price(-850)
        purchase.get_price()
        amount = 500 * -850 * (1 - 0.08 / 100)
        self.assertNotEqual(purchase.get_price(), amount)