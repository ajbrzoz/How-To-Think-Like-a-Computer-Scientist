# Exercise 15.8.8

# Using the turtle graphics module, write a recursive program to display a Koch snowflake.

from turtle import *


def koch(length, depth):
    if depth == 0:
        forward(length)
    else:
        koch(length/3, depth-1)
        right(60)
        koch(length/3, depth-1)
        left(120)
        koch(length/3, depth-1)
        right(60)
        koch(length/3, depth-1)
        
koch(200, 3)
left(120)
koch(200, 3)
left(120)
koch(200, 3)
