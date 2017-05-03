# Exercise 9.22.9

# Write a function that recognizes palindromes.


def is_palindrome(my_str):
    count = 0
    palin = True
    while count < len(my_str) and palin:
        if my_str[0] == my_str[-1]:
            my_str = my_str[1:-1]
            is_palindrome(my_str)
        else:
            palin = False
    return palin
