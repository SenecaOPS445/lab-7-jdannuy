#!/usr/bin/env python3

from lab7c import Time, sum_times, change_time

# Creating Time objects
t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

# Time duration to add
td = Time(0, 50, 0)

# Summing time objects
tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)

# Adding 1800 seconds (30 minutes) to t3
t3_updated = change_time(t3, 1800)

# Displaying results
print(f"{t1} + {td} --> {tsum1}")
print(f"{t2} + {td} --> {tsum2}")
print(f"09:50:00 + 1800 sec --> {t3_updated}")
