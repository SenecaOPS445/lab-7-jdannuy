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

    def format_time(self):
        """Return a formatted string representing the time."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        """Convert a time object to the total number of seconds since midnight."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def sum_times(self, other_time):
        """Add two Time objects and return a new Time object with the sum."""
        total_seconds = self.time_to_sec() + other_time.time_to_sec()
        return sec_to_time(total_seconds)  # Now using the external function

    def valid_time(self):
        """Check for the validity of the time object attributes."""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def change_time(self, seconds):
        """Modify the current time by adding the given number of seconds."""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

# Now defining `sec_to_time()` as a standalone function
def sec_to_time(seconds):
    """Convert seconds to a Time object."""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return Time(hours % 24, minutes, seconds)  # Ensure it wraps around 24-hour format
