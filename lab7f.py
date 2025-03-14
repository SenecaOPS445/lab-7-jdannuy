class Time:
    """Time class that supports addition and other time operations."""

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor to initialize time."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation of the time object."""
        return self.format_time()

    def __repr__(self):
        """Return a string representation with dots."""
        return f"{self.hour:02d}.{self.minute:02d}.{self.second:02d}"

    def format_time(self):
        """Return the time in 'hh:mm:ss' format."""
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def valid_time(self):
        """Check if the current time is valid."""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def sum_times(self, other_time):
        """Sum two times and return a new Time object."""
        total_seconds = (self.hour * 3600 + self.minute * 60 + self.second) + \
                        (other_time.hour * 3600 + other_time.minute * 60 + other_time.second)
        return self.sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify the time by adding seconds."""
        total_seconds = (self.hour * 3600 + self.minute * 60 + self.second) + seconds
        new_time = self.sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    @staticmethod
    def sec_to_time(seconds):
        """Convert seconds into a Time object."""
        seconds %= 86400  # Ensure seconds do not exceed one day (86400 seconds)
        hour = seconds // 3600
        seconds %= 3600
        minute = seconds // 60
        second = seconds % 60
        return Time(hour, minute, second)

    def __add__(self, other_time):
        """Allow adding two Time objects."""
        return self.sum_times(other_time)
