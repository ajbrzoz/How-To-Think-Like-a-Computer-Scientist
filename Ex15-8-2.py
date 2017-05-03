# Exercise 15.8.2

# Write a recursive function to reverse a list.


def rev_lst(lst):
    if len(lst) <= 1:
        return lst
    else:
        return [lst[-1]] + rev_lst(lst[:-1])
