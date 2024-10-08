from decimal import Decimal

class CarClass:

    def __init__(self, model: str, year: str, price = Decimal(0)):
        self.model = model
        self.year = year
        self.price = price

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_price(self, price):
        if price > 0:
            self.price = price

    def get_price(self):
        return self.price

    def price_discount(self, percentage):
        if 0 < percentage <= 100:
            self.price -= self.price * (percentage / 100)