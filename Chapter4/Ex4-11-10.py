# Exercise 4.11.10

# Write a program to draw a face of a clock that looks something like this:
# http://interactivepython.org/runestone/static/thinkcspy/_images/tess_clock1.png

import turtle

foo = turtle.Turtle()
foo.shape('turtle')
foo.color('blue')
foo.up()
foo.stamp()
for n in range(12):
    foo.forward(90)
    fo.down()
    foo.forward(5)
    foo.up()
    foo.forward(20)
    foo.stamp()
    foo.backward(115)
    foo.left(30)
