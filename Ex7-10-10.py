# Exercise 7.10.10

# Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether
# the triangle is right-angled. Assume that the third argument to the function is always the longest side.
# It will return True if the triangle is right-angled, or False otherwise.


def is_rightangled(a, b, c):
    x = a ** 2 + b ** 2
    y = c ** 2
    if abs(x - y) < 0.001:
        return True
    else:
        return False


# Exercise 7.10.11

# Extend the above program so that the sides can be given to the function in any order.


def is_rightangled(a, b, c):
  ll = [a, b, c]
  y = max(ll)**2
  ll.remove(max(ll))
  x = ll[0]**2 + ll[1]**2
  if abs(x - y) < 0.001:
    return True
  else:
    return False
