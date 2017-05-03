# Exercise 10.30.25

# Count how many words occur in a list up to and including the first occurrence of the word “sam”.


def until_sam(lst):
    count = 0
    index = 0
    if len(lst) > 0:
        while index < len(lst) and lst[index] != "sam":
            count += 1
            index += 1
        if lst[index] == 'sam':
            count += 1   
    return count
