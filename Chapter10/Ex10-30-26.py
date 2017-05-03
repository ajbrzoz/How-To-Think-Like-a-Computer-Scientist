# Exercise 10.30.26

# Although Python provides us with many list methods, it is good practice and very instructive to think about
# how they are implemented. Implement a Python function that works like the following:

#    count
#    in
#    reverse
#    index
#    insert


def func_count(lst, item):
    counter = 0
    for n in lst:
        if n == item:
            counter += 1
    return counter


def func_in(lst, item):
    isin = False
    index = 0
    while not isin and index < len(lst):
        if lst[index] == item:
            isin = True
        index += 1
    return isin


def func_reversal(lst):
    return lst[::-1]


def func_index(lst, item):
    index = 0
    if len(lst) > 0:
        while index < len(lst) and lst[index] != item:
            index += 1
    else:
        return -1
    return index


def func_insert(lst, ind, item):
    newlst = []
    for i in range(len(lst)):
        if i == ind:
            newlst.append(item)
        newlst.append(lst[i])
    return newlst
