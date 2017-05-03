# Exercise 10.30.18

# Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return
# the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)

import random

ll = [random.randrange(0, 1001) for n in range(100)]


def maxim(lll):
    maximum = 0
    for l in lll:
        if l > maximum:
            maximum = l
    return maximum


print(maxim(ll))
