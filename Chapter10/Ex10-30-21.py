# Exercise 10.30.21

# Sum up all the even numbers in a list.


def sum_even(ll):
    return sum([n for n in ll if n % 2 == 0])
