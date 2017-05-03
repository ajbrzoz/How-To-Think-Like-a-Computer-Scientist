# Approximating the Value of Pi

# In this lab, we will approximate the value of pi using a technique known as Monte
# Carlo Simulation.  The game that we will use for this simulation is “darts”. We will “randomly” throw a number of
# darts at a specially configured dartboard. The piece of wood is exactly two units square so that the round board
# fits perfectly inside the square. If we throw a whole bunch of darts and let them randomly land on the square
# piece of wood, some will also land on the dartboard. The number of darts that land on the dartboard, divided by
# the number that we throw total, will be in the ratio described above (pi/4). Multiply by 4 and we have pi.


import random
import turtle

fred = turtle.Turtle()
fred.up()

wn = turtle.Screen()
wn.setworldcoordinates(-1, -1, 1, 1)


def draw_polygon(t, side_length, num_sides):
    turn_angle = 360 / num_sides
    for n in range(num_sides):
        t.forward(side_length)
        t.right(turn_angle)


def draw_circle(any_turtle, radius):
    circumference = 2 * 3.1415 * radius
    side_length = circumference / 360
    draw_polygon(any_turtle, side_length, 360)


fred.up()
fred.goto(0, 1)
fred.down()
fred.speed('fastest')
draw_circle(fred, 1)
fred.up()
fred.goto(0, 0)

numdarts = 100
inside_count = 0

for i in range(numdarts):
    randx = random.random()
    randy = random.random()

    x = randx * random.randrange(-1, 2, 2)
    y = randy * random.randrange(-1, 2, 2)

    fred.goto(x, y)

    if fred.distance(0, 0) > 1:
        fred.color('red')
        fred.dot()
    else:
        fred.color('blue')
        fred.dot()
        inside_count += 1


def compute_pi(darts, inside):
    pi = (inside / darts) * 4
    return pi


print(compute_pi(numdarts, inside_count))

wn.exitonclick()
