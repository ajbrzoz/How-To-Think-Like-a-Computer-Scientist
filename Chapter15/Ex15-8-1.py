# Exercise 15.8.1

# Write a recursive function to compute the factorial of a number.


def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)
