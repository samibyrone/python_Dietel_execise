import datetime
import unittest

from Chapter3.From_java_Dietel_to_python_Chapter3.target_heart_rate import HeartRate

class TestTargetHeartBeatRate(unittest.TestCase):

    def setUp(self):
        HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)

    def test_for_person_heart_rate_first_name(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        first_name = "Adewale"
        self.assertEqual(heart_rate.get_first_name(), first_name)
        first_name = heart_rate.set_first_name("bolaji")
        self.assertEqual(heart_rate.set_first_name("bolaji"), first_name)

    def test_for_person_heart_rate_last_name(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        last_name = "Ehinmode"
        self.assertEqual(heart_rate.get_last_name(), last_name)
        last_name = heart_rate.set_last_name("Opemiposi")
        self.assertEqual(heart_rate.set_last_name("Opemiposi"), last_name)

    def test_for_person_heart_rate_gender(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        gender = "Male"
        self.assertEqual(heart_rate.get_gender(), gender)
        gender = heart_rate.set_gender("Female")
        self.assertEqual(heart_rate.set_gender("Female"), gender)

    def test_for_person_heart_rate_birth_day(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        day = 20
        self.assertEqual(heart_rate.get_day(), day)
        day = heart_rate.set_day(27)
        self.assertEqual(heart_rate.set_day("27"), day)

    def test_for_person_heart_rate_birth_month(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        month = 4
        self.assertEqual(heart_rate.get_month(), month)
        month = heart_rate.set_month(12)
        self.assertEqual(heart_rate.set_month(12), month)

    def test_for_person_heart_rate_birth_year(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        year = 2017
        self.assertEqual(heart_rate.get_year(), year)
        year = heart_rate.set_year(2002)
        self.assertEqual(heart_rate.set_year(2002), year)

    def test_for_person_heart_rate_age(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        current_age = datetime.datetime.now().year
        age = current_age - heart_rate.get_year()
        self.assertEqual(heart_rate.get_age(), age)

    def test_for_person_heart_rate_birth_year_with_leap_year(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        heart_rate.set_day(29)
        heart_rate.set_month(2)
        heart_rate.set_year(2020)
        self.assertEqual(heart_rate.get_age(), 4)

    def test_for_person_heart_beat_rate_at_age_220(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        heart_rate.set_day(2)
        heart_rate.set_month(10)
        heart_rate.set_year(1804)
        self.assertEqual(heart_rate.get_maximum_heart_beat_rate(), 0)

    def test_for_person_heart_beat_rate(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        current_year = datetime.datetime.now().year
        age = current_year - heart_rate.get_year()
        self.assertEqual(heart_rate.get_maximum_heart_beat_rate(), 220 - age)

    def test_for_person_heart_beat_rate_range(self):
        heart_rate = HeartRate("Adewale", "Ehinmode", "Male", 20, 4, 2017)
        heart_beat_rate = heart_rate.get_maximum_heart_beat_rate()
        heart_beat_rate_range = f"{heart_beat_rate * 0.5:.0f} - {heart_beat_rate * 0.85:.0f}"
        self.assertEqual(heart_rate.get_maximum_heart_beat_rate_range(), heart_beat_rate_range)