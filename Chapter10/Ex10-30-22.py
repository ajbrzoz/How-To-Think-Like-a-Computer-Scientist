# Exercise 10.30.22

# Sum up all the negative numbers in a list.


def sum_neg(ll):
    return sum([n for n in ll if n < 0])
