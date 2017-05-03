# Exercise 8.13.7

# Write a function to remove all the red from an image:
# http://interactivepython.org/runestone/static/thinkcspy/_static/LutherBellPic.jpg
# For this and the following exercises, use the luther.jpg photo.

import image

img = image.Image('luther.jpg')
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1, 15)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        g = p.getGreen()
        b = p.getBlue()
        newp = image.Pixel(0, g, b)
        img.setPixel(col, row, newp)

img.draw(win)
