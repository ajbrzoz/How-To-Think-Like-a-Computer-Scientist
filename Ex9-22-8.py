# Exercise 9.22.8

# Write a function that removes all occurrences of a given letter from a string.


def remove_letter(letter, string):
    new_str = ''
    for c in string:
        if c != letter:
            new_str += c
    return new_str
