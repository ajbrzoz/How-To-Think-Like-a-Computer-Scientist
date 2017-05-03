# Exercise 9.22.20

# Write a function called remove_dups that takes a string and creates a new string by only adding those characters
# that are not already present. In other words, there will never be a duplicate letter added to the new string.


def remove_dups(astring):
    newstr = ""
    for char in astring:
        if char not in newstr:
            newstr += char
    return newstr
