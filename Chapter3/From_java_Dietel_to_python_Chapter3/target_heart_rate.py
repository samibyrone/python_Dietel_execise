from datetime import datetime

class HeartRate:

    def __init__(self, first_name, last_name, gender, day, month, year):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.day = day
        self.month = month
        self.year = year

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

    def set_day(self, day):
        self.day = day

    def get_day(self):
        return self.day

    def set_month(self, month):
        self.month = month

    def get_month(self):
        return self.month

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year

    def get_maximum_heart_beat_rate(self):
        return 220 - self.get_age()

    def get_maximum_heart_beat_rate_range(self):
        heart_beat_rate_range = self.get_maximum_heart_beat_rate()
        return f"{heart_beat_rate_range * 0.5:.0f} - {heart_beat_rate_range * 0.85:.0f}"
