"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time

#Attempt 1

start_time = time.time()

total = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i

print total

print time.time() - start_time, "seconds\n"

"""
These 'improved' versions are only really more efficient with numbers
larger than 1000
"""

#Improvement 1

start_time = time.time()

total = 0
for i in xrange(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i

print total

print time.time() - start_time, "seconds\n"

#Improvement 2

start_time = time.time()

total = sum([i for i in xrange(1, 1000) if i % 3 == 0 or i % 5 == 0])

print total

print time.time() - start_time, "seconds\n"
