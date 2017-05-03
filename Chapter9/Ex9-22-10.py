# Exercise 9.22.10

# Write a function that counts how many times a substring occurs in a string.


def count(substr, my_str):
    counter = 0
    ix = 0
    while ix < len(my_str):
        ix = my_str.find(substr, ix)
        if ix == -1:
            return counter
        counter += 1
        ix = my_str.find(substr, ix+1)
    return counter
