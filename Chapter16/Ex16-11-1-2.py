# Exercise 16.11.1

# Add a distanceFromPoint method that works similar to distanceFromOrigin except that it takes a Point as a
# parameter and computes the distance between that point and self.

# Exercise 16.12.2

# Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about 
# the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)


import math


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance_from_point(self, other_p):
        dx = other_p.get_x() - self.x
        dy = other_p.get_y() - self.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def reflect_x(self):
        rx = self.x
        ry = -self.y
        return Point(rx, ry)
