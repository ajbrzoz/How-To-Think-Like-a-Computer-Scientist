# Exercise 9.22.7

# Write a function that mirrors its argument.


def mirror(mystr):
    mirror_str = mystr + mystr[::-1]
    return mirror_str
