# Exercise 10.30.24

# Sum all the elements in a list up to but not including the first even number.


def sum_excl(lst):
    summ = 0
    index = 0
    while lst[index] % 2 == 0 and index < len(lst):
        summ += lst[index]
        index += 1
    return summ
