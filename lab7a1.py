#!/usr/bin/env python3
<<<<<<< HEAD
# Student ID: jdannuy

from lab7a import *  # Import Time class and functions

# Creating Time objects
t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

td = Time(0, 50, 0)  # Time to add

# Calculate the sums
tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)
tsum3 = sum_times(t3, td)   

# Format and print the times
ft = format_time
print(ft(t1), '+', ft(td), '-->', ft(tsum1))
print(ft(t2), '+', ft(td), '-->', ft(tsum2))
print(ft(t3), '+', ft(td), '-->', ft(tsum3))
=======
# Student ID: [seneca_id]
from lab7a import *
t1 = Time(8,0,0)
t2 = Time(8,55,0)
t3 = Time(9,50,0)

td = Time(0,50,0)

tsum1 = sum_times(t1,td)
tsum2 = sum_times(t2,td)
tsum3 = sum_times(t3,td)   

ft = format_time
print(ft(t1),'+',ft(td),'-->',ft(tsum1))
print(ft(t2),'+',ft(td),'-->',ft(tsum2))
print(ft(t3),'+',ft(td),'-->',ft(tsum3))
>>>>>>> 3af12a3a820bd18480340b5b26c16d816d427480
