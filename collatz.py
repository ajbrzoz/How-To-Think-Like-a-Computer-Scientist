# Experimenting with the 3n+1 Sequence

# In this lab we will try to gain a bit more information about the 3n+1 sequence. 
# Count the number of iterations it takes to stop.
# Repeat the call to seq3np1 using a range of values, up to and including an upper bound.
# Use the turtle graphics to graph the number of iterations. 
# Keep track of the maximum number of iterations.
# Experiment with different ranges of starting values.

import turtle

collatz = turtle.Turtle()
bg = turtle.Screen()
bg.setworldcoordinates(0, 0, 50, 100)


def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n != 1:
        if n % 2 == 0:  # n is even
            n = n // 2
        else:  # n is odd
            n = n * 3 + 1
        count += 1
    return count


start = range(1, 50)
maxSoFar = 0            # maximum value of function
maxIter = 0             # n value for maxSoFar

for n in start:
    m = seq3np1(n)
    if m > 100:
        collatz.goto(n, 100)
    else:
        collatz.goto(n, m)
    if m > maxSoFar:
        maxSoFar = m
        maxIter = n

print(maxIter, maxSoFar)

start = range(51, 100)  # experiment with higher values

for n in start:
    m = seq3np1(n)
    if m > maxSoFar:
        print(n, m)
        break


def func(aim, max_cap, min_cap, maxi=0, mini=0):
    while maxi != aim:
        print(maxi, mini)
    if mini == aim:
        maxi = mini
    if maxi >= max_cap:
        maxi = 0
    else:
        mini = min_cap
        print(maxi, mini)
        maxi = mini
        print(maxi, mini)
        mini = 0
        print(maxi, mini)
        mini = min_cap
        print(maxi, mini)
        maxi += max_cap - mini
        print(maxi, mini)


# return func(aim, max_cap, min_cap, maxi, mini)


func(2, 4, 3)