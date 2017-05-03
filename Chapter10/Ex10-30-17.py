# Exercise 10.13.17

# Create a list containing 100 random integers between 0 and 1000. Write a function called average that will
# take the list as a parameter and return the average.

import random


def average(l):
    return sum(l) / len(l)


ll = [random.randrange(0, 1001) for n in range(100)]
print(average(ll))
