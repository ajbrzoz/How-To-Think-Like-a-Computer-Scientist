# Exercise 8.13.8

# Write a function to convert the image
# (http://interactivepython.org/runestone/static/thinkcspy/_static/LutherBellPic.jpg).
# to grayscale.

from sys import argv
from PIL import Image

script, image = argv

img = Image.open(image)

for row in range(img.height):
    for col in range(img.width):
        pixy = img.load()
        colours = pixy.__getitem__((col, row))
        av = sum(colours)//len(colours)
        pixy[col, row] = (av, av, av)

img.show()
