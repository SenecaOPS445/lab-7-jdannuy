#!/usr/bin/env python3

class Time:
    def __init__(self, hours, minutes, seconds):
        if not (isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int)):
            raise ValueError("All arguments must be integers")
        if not (0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError("Minutes and seconds must be in the range [0, 59]")
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def to_seconds(self):
        """Convert time to total seconds."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        """Convert seconds back to a Time object."""
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

def sum_times(t1, t2):
    """Sum two Time objects and return the resulting Time object."""
    total_seconds = t1.to_seconds() + t2.to_seconds()
    return Time.from_seconds(total_seconds)

def change_time(t, seconds_to_add):
    """Add seconds to a Time object and return the resulting Time object."""
    total_seconds = t.to_seconds() + seconds_to_add
    # Ensure total seconds don't exceed 24 hours (86400 seconds in a day)
    total_seconds %= 86400  # This line makes sure the result is within a 24-hour period
    return Time.from_seconds(total_seconds)

def sec_to_time(seconds):
    """Convert seconds to a Time object."""
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds = seconds % 60
    return Time(hours, minutes, seconds)

def format_time(t):
    """Return the formatted time as HH:MM:SS."""
    return str(t)

def time_to_sec(t):
    """Convert a Time object to total seconds."""
    return t.to_seconds()

# Testing the functions
if __name__ == "__main__":
    # Create Time objects
    t1 = Time(8, 0, 0)
    t2 = Time(8, 55, 0)
    t3 = Time(9, 50, 0)

    # Time to add
    td = Time(0, 50, 0)

    # Sum times
    tsum1 = sum_times(t1, td)
    tsum2 = sum_times(t2, td)

    # Change time by adding 1800 seconds (30 minutes)
    t3_updated = change_time(t3, 1800)  # Adding 1800 seconds (30 minutes)

    # Print results
    print(format_time(t1), '+', format_time(td), '-->', format_time(tsum1))
    print(format_time(t2), '+', format_time(td), '-->', format_time(tsum2))
    print('09:50:00 + 1800 sec -->', format_time(t3_updated))
