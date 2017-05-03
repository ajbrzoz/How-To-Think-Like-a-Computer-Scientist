# Exercise 9.22.12

# Write a function that removes all occurrences of a string from another string.


def remove_all(substr, my_str):
    ix = 0
    while ix < len(my_str):
        ix = my_str.find(substr, ix)
        if ix == -1:
            return my_str
        my_str = my_str[:ix] + my_str[(ix + len(substr)):]
        ix = my_str.find(substr, ix)
    return my_str
