from decimal import Decimal


class PetrolPurchase:

    def __init__(self, location: str, petrol_type:str, quantity:int, price:int, price_discount:float):
        self.location = location
        self.petrol_type = petrol_type
        self.quantity = quantity
        self.price = price
        self.price_discount = price_discount

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_petrol_type(self, petrol_type):
        self.petrol_type = petrol_type

    def get_petrol_type(self):
        return self.petrol_type

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_price_discount(self, price_discount):
        self.price_discount = price_discount

    def get_price_discount(self):
        return self.price_discount

    def get_purchase_price(self):
        cost = self.quantity * self.price
        discount = cost * (self.price_discount / 100)
        return cost - discount