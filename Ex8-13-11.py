# Exercise 8.13.11

# Write a function to uniformly enlarge an image by a factor of 2 (double the size).
# For this and the following exercises, use the luther.jpg photo:
# http://interactivepython.org/runestone/static/thinkcspy/_static/LutherBellPic.jpg

import image
import sys

sys.setExecutionLimit(600000)


def double(oldpic):
    oldh = oldpic.getHeight()
    oldw = oldpic.getWidth()

    newpic = image.EmptyImage(oldw * 2, oldh * 2)

    for row in range(oldh):
        for col in range(oldw):
            oldpix = oldpic.getPixel(col, row)

            newpic.setPixel(2 * col, 2 * row, oldpix)
            newpic.setPixel(2 * col + 1, 2 * row, oldpix)
            newpic.setPixel(2 * col, 2 * row + 1, oldpix)
            newpic.setPixel(2 * col + 1, 2 * row + 1, oldpix)

    return newpic


win = image.ImageWin()
img = image.Image("luther.jpg")

bigimg = double(img)
bigimg.draw(win)
