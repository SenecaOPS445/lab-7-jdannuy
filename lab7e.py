#!/usr/bin/env python3
# Student ID: jdannuy

class Time:
    """Simple object type for time of the day."""
    
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for the Time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation of the time object."""
        return self.format_time()

    def __repr__(self):
        """Return a string representation of the time object using dots instead of colons."""
        return f"{self.hour:02d}.{self.minute:02d}.{self.second:02d}"

    def format_time(self):
        """Return a formatted string representing the time."""
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def valid_time(self):
        """Check if the time is valid."""
        if not (0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60):
            return False
        return True

    def sum_times(self, other_time):
        """Return a new Time object that is the sum of this time and another time."""
        total_seconds = (self.hour * 3600 + self.minute * 60 + self.second) + \
                        (other_time.hour * 3600 + other_time.minute * 60 + other_time.second)
        return self.sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify the current time by adding the given number of seconds."""
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second + seconds
        new_time = self.sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    @staticmethod
    def sec_to_time(seconds):
        """Convert seconds into a Time object."""
        seconds %= 86400  # Ensure we don't exceed 24 hours
        hour = seconds // 3600
        seconds %= 3600
        minute = seconds // 60
        second = seconds % 60
        return Time(hour, minute, second)
