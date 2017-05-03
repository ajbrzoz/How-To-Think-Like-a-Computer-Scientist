# Plotting a Sine Wave

# In this exercise, we will use our turtle to plot a simple math function, 
# the sine wave. For this lab, we will use the math library to generate 
# the values that we need. 

import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(0, -1.25, 360, 1.25)

fred = turtle.Turtle()

for angle in range(0, 360):
    x = angle
    y = math.sin(math.radians(angle))
    fred.goto(x, y)

wn.exitonclick()
