import datetime
import unittest

from Chapter3.From_java_Dietel_to_python_Chapter3.health_records import HealthRecord


class TestHealthRecords(unittest.TestCase):

    def test_setup(self):
        HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)

    def test_for_profile_health_record_first_name(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        first_name = "Sammy"
        self.assertEqual(health_records.get_first_name(), first_name)
        first_name = health_records.set_first_name("bolaji")
        self.assertEqual(health_records.set_first_name("bolaji"), first_name)

    def test_for_profile_health_record_last_name(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        last_name = "Olamide"
        self.assertEqual(health_records.get_last_name(), last_name)
        last_name = health_records.set_last_name("Chibuzor")
        self.assertEqual(health_records.set_last_name("Chibuzor"), last_name)

    def test_for_profile_health_record_gender(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        gender = "Male"
        self.assertEqual(health_records.get_gender(), gender)
        gender = health_records.set_gender("Female")
        self.assertEqual(health_records.set_gender("Female"), gender)

    def test_for_profile_health_record_for_birth_day(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        day_of_birth = 25
        self.assertEqual(health_records.get_birth_day(), day_of_birth)
        day_of_birth = health_records.set_birth_day(17)
        self.assertEqual(health_records.set_birth_day(17), day_of_birth)

    def test_for_profile_health_record_for_birth_month(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        month_of_birth = 8
        self.assertEqual(health_records.get_birth_month(), month_of_birth)
        month_of_birth = health_records.set_birth_month(12)
        self.assertEqual(health_records.set_birth_month(12), month_of_birth)

    def test_for_profile_health_record_for_birth_year(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        year_of_birth = 2005
        self.assertEqual(health_records.get_birth_year(), year_of_birth)
        year_of_birth = health_records.set_birth_year(1879)
        self.assertEqual(health_records.set_birth_year(1879), year_of_birth)

    def test_for_profile_health_record_estimated_age(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        current_age = datetime.datetime.now().year
        age = current_age - health_records.get_birth_year()
        self.assertEqual(health_records.get_age(), age)

    def test_for_profile_health_record_for_birth_year_with_leap_year(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        health_records.set_birth_day(29)
        health_records.set_birth_month(2)
        health_records.set_birth_year(2001)
        self.assertEqual(health_records.get_age(), 23)

    def test_for_profile_health_record_for_height_in_inches(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        height_in_inches = 68
        self.assertEqual(health_records.get_height(), height_in_inches)
        height_in_inches = health_records.set_height(72)
        self.assertEqual(health_records.set_height(72), height_in_inches)

    def test_for_profile_health_record_with_zero_height_in_inches(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        height_in_inches = 68
        self.assertEqual(health_records.get_height(), height_in_inches)
        height_in_inches = health_records.set_height(0)
        self.assertEqual(health_records.set_height(0), height_in_inches)

    def test_for_profile_health_record_for_weight_in_pounds(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        weight_in_pounds = 145
        self.assertEqual(health_records.get_weight(), weight_in_pounds)
        weight_in_pounds = health_records.set_weight(157)
        self.assertEqual(health_records.set_weight(157), weight_in_pounds)

    def test_for_profile_health_record_with_zero_weight_in_pounds(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        weight_in_pounds = 145
        self.assertEqual(health_records.get_weight(), weight_in_pounds)
        weight_in_pounds = health_records.set_weight(0)
        self.assertEqual(health_records.set_weight(0), weight_in_pounds)

    def test_for_profile_health_record_for_body_mass_index(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        if health_records.height <= 0: return float('inf') if health_records.height == 0 else float('nan')
        return (health_records.weight * 703) / (health_records.height * health_records.height)
        self.assertEqual(health_records.get_body_mass_index(), float('inf'))

    def test_for_profile_health_record_maximum_heart_rate(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        current_age = datetime.datetime.now().year
        age = current_age - health_records.get_birth_year()
        self.assertEqual(health_records.get_maximum_heart_beat_rate(), 220 - age)

    def test_for_profile_health_record_maximum_heart_rate_range(self):
        health_records = HealthRecord("Sammy", "Olamide", "Male", 25, 8, 2005, 68, 145)
        heart_beat = health_records.get_maximum_heart_beat_rate()
        heart_beat_range = f"{heart_beat * 0.5:.0f} - {heart_beat * 0.85:.0f}"
        self.assertEqual(health_records.get_targeted_heart_beat_rate_range(), heart_beat_range)