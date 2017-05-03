# Exercise 16.11.3

# The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”). The coefficients a and b 
# completely describe the line. Write a method in the Point class so that if a point instance is given 
# another point, it will compute the equation of the straight line joining the two points. It must 
# return the two coefficients as a tuple of two values. 

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def get_line_to(self, other):
        if self.x == other.x or self.y == other.y:
            return None
        a = (self.y-other.y)//(self.x-other.x)
        b = other.y - a*other.x
        return (a,b)
