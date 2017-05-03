# Exercise 15.8.9

# Write a program to solve the following problem: You have two jugs: a 4-gallon jug and a 3-gallon jug. 
# Neither of the jugs have markings on them. There is a pump that can be used to fill the jugs with water. 
# How can you get exactly two gallons of water in the 4-gallon jug?

# Exercise 15.8.10

# Generalize the problem above so that the parameters to your solution include the sizes of each jug and 
# the final amount of water to be left in the larger jug.

import math


def jug(aim, max_cap, min_cap, maxi=0, mini=0):
    """
    Args:
        aim (int): final amount of water to be left in larger jug
        max_cap (int): capacity of larger jug
        min_cap (int): capacity of smaller jug
        maxi (int): current amount of water in larger jug
        mini (int): current amount of water in smaller jug
    """

    # error handling
    if any(x <= 0 for x in (aim, max_cap, min_cap)):
        raise ValueError("Capacity of each jug must be positive.")

    if aim > max_cap:
        raise ValueError("The final amount of water cannot exceed the larger jug's capacity.")

    if aim % math.gcd(max_cap, min_cap) != 0:
        raise ValueError("The final amount of water to be left in the larger jug must be divisible by "
                         "the greatest common divisor of jugs' capacities.")

    def inner_jug(aim, max_cap, min_cap, maxi, mini):
        print(maxi, mini)

        if maxi == aim:
            return

        # if water in smaller jug reaches desired level, pour water out of larger jug
        # and fill it with water from smaller jug
        if mini == aim:
            maxi = mini
            print(maxi, mini)
            return

        while maxi < max_cap:
            mini += min_cap     # fill smaller jug up
            print(maxi, mini)

            am = min(mini, max_cap - maxi)  # amount of water remaining to fill larger jug up
            maxi += am
            print(maxi, mini)

            mini -= am
            print(maxi, mini)

        inner_jug(aim, max_cap, min_cap, mini, 0)
