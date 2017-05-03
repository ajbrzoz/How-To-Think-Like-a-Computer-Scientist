# Letter Count Histogram

# Create a function that will take a string and create a histogram of # the number of times each letter occurs.
# Make sure it is in #alphabetical order from left to right.


import turtle

bob = turtle.Turtle()


def letter_count(text, t, color):
    """t - Turtle object"""

    count = {}
    for n in text:
        m = text.count(n)
        count[str(n)] = m  # keep the count in a dictionary
    letters = count.keys()
    letters.sort()

    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, 10, 20)
    t.forward(1)

    for l in letters:
        ind = count[str(l)]
        t.fillcolor(color)
        t.left(180)
        t.begin_fill()
        for i in range(2):
            t.right(90)
            t.forward(ind)
            t.right(90)
            t.forward(1)
        t.end_fill()
        t.right(180)
        t.forward(1)
        if ind == 1:
            print('{} : {} time'.format(l, ind))
        else:
            print('{} : {} times'.format(l, ind))


lettercount('foobar', bob, 'lime')
