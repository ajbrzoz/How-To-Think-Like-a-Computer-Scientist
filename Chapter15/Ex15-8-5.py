# Exercise 15.8.5

# Write a recursive function to compute the Fibonacci sequence.


# recursive version
def fibonacci_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


# iterative version
def fibonacci_it(n):
    if n == 0 or n == 1:
        return n
    else:
        fib = [0] * (n + 1)
        fib[0] = 0
        fib[1] = 1
        for x in range(2, n + 1):
            fib[x] = fib[x - 1] + fib[x - 2]
        return fib[n]
