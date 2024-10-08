from datetime import datetime

import unittest

from Chapter3.From_java_Dietel_to_python_Chapter3.clock import Clock


class TestMyClockTimer(unittest.TestCase):

    def test_setup(self):
       Clock(12, 30, 30)

    def test_to_initialize_the_time(self):
        timer = Clock(12, 30, 30)
        hourly = 12
        minutes = 30
        seconds = 30
        self.assertEqual(timer.get_hour, hourly)
        self.assertEqual(timer.get_minute, minutes)
        self.assertEqual(timer.get_second, seconds)

    def test_to_set_invalid_hour(self):
        timer = Clock(12, 30, 30)
        hourly = timer.set_hours(24)
        self.assertEqual(timer.get_hour, 0, hourly)

    def test_to_set_invalid_minute(self):
        timer = Clock(12, 30, 30)
        minutes = timer.set_minutes(60)
        self.assertEqual(timer.get_minute, 0, minutes)

    def test_to_set_invalid_seconds(self):
        timer = Clock(12, 30, 30)
        seconds = timer.set_seconds(60)
        self.assertEqual(timer.get_second, 0, seconds)

    def test_to_display_time_format(self):
        timer = Clock(8, 30, 45)
        self.assertEqual(timer.time_format(), "08:30:45")

    def test_to_display_time_with_minimum_value(self):
        timer = Clock(0, 0, 0)
        self.assertEqual(timer.time_format(),"00:00:00")

    def test_to_display_time_with_maximum_value(self):
        timer = Clock(23, 59, 59)
        self.assertEqual(timer.time_format(),"23:59:59")

