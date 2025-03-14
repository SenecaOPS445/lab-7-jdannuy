#!/usr/bin/env python3
<<<<<<< HEAD
# Student ID: jdannuy

class Time:
    """Simple object type for time of the day."""
    
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for the Time object"""
=======
# Student ID: [seneca_id] 
class Time:
    """Simple object type for time of the day.
        data attributes: hour, minute, second
        function attributes: __init__, __str__, __repr__
                            time_to_sec, format_time,
                            change_time, sum_time
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
>>>>>>> 3af12a3a820bd18480340b5b26c16d816d427480
        self.hour = hour
        self.minute = minute
        self.second = second

<<<<<<< HEAD
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
=======
    def format_time(self):
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objests and return the sum."""
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        sum = sec_to_time(self_sec + t2_sec)
        return sum

    def change_time(self, seconds):
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second 
        return None

    def time_to_sec(self):
        '''convert a time object to a single integer representing the 
        number of seconds from mid-night'''
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in 
        hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
>>>>>>> 3af12a3a820bd18480340b5b26c16d816d427480
