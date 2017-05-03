# Exercise 10.30.20

# Write a function to count how many odd numbers are in a list.


def count_odd(ll):
    return len([n for n in ll if n % 2 != 0])
