from datetime import datetime

class HealthRecord:

    def __init__(self, first_name, last_name, gender, birth_day, birth_month, birth_year, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.height = height
        self.weight = weight

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_birth_day(self, birth_day):
        self.birth_day = birth_day

    def get_birth_day(self):
        return self.birth_day

    def set_birth_month(self, birth_month):
        self.birth_month = birth_month

    def get_birth_month(self):
        return self.birth_month

    def set_birth_year(self, birth_year):
        self.birth_year = birth_year

    def get_birth_year(self):
        return self.birth_year

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year

    def get_body_mass_index(self):
        if self.height <= 0: return float('inf') if self.height == 0 else float('nan')
        return (self.weight * 703) / (self.height * self.height)

    def get_maximum_heart_beat_rate(self):
        return 220 - self.get_age()

    def get_targeted_heart_beat_rate_range(self):
        maximum_heart_beat_rate = self.get_maximum_heart_beat_rate()
        return f"{maximum_heart_beat_rate * 0.5:.0f} - {maximum_heart_beat_rate * 0.85:.0f}"

