# Exercise 16.11.5

# Add a method called move that will take two parameters, call them dx and dy. The method will cause the point
# to move in the x and y direction the number of units given.


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
