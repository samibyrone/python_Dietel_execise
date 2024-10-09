from datetime import datetime

class Clock:

    def __init__(self, hour:int, minute:int, second:int):
        self._hour = hour
        self._minute = minute
        self._second = second
        self.time_validation()

    def set_hours(self, hours):
        self._hour = hours
        self.time_validation()

    @property
    def get_hour(self):
        return self._hour

    def set_minutes(self, minutes):
        self._minute = minutes
        self.time_validation()

    @property
    def get_minute(self):
        return self._minute

    def set_seconds(self, seconds):
        self._second = seconds
        self.time_validation()

    @property
    def get_second(self):
        return self._second

    def time_validation(self):
        if self._hour > 23 or self._minute > 59 or self._second > 59:
            self._hour = 0
            self._minute = 0
            self._second = 0

    def time_format(self):
        return f"{self._hour:06}:{self._minute:30}:{self._second:30}"