# Exercise 16.11.6

# Given three points that fall on the circumference of a circle, find the center and radius of the circle.


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

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def mid(self, other):
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)

    def get_line_to(self, other):
        if self.x == other.x or self.y == other.y:
            return None
        a = (self.y - other.y) / (self.x - other.x)
        b = other.y - a * other.x
        return (a, b)

    def distance_from_point(self, other_p):
        dx = other_p.get_x() - self.x
        dy = other_p.get_y() - self.y
        return (dx ** 2 + dy ** 2) ** 0.5


def circle(p1, p2, p3):
    m1 = p1.mid(p2)
    m3 = p3.mid(p1)
    line1 = p1.get_line_to(p2)
    line3 = p3.get_line_to(p1)
    sym1 = (-1 / line1[0], m1.y + ((1 / line1[0]) * m1.x))
    sym3 = (-1 / line3[0], m3.y + ((1 / line3[0]) * m3.x))
    print(sym1, sym3)
    xx = (sym3[1] - sym1[1]) / (sym1[0] - sym3[0])
    yy = sym1[0] * xx + sym1[1]
    circle_center = Point(xx, yy)
    radius = p3.distance_from_point(circle_center)
    return circle_center.x, circle_center.y, radius
