# Exercise 8.13.15

# Research the Sobel edge detection algorithm and implement it.


from sys import argv
from PIL import Image
from urllib.request import urlopen
from io import BytesIO
import validators

if len(argv) == 2:
    script, image = argv
else:
    image = input('Enter the name or url of your image: ')

if validators.url(image):
    link = urlopen(image)
    img = Image.open(BytesIO(link.read()))
else:
    img = Image.open(image)

pixy = img.load()

for x in range(1, img.width - 1):
    for y in range(1, img.height - 1):
        gx = 0
        gy = 0

        r, g, b = pixy[x - 1, y - 1]
        intensity = r + g + b

        gx += -intensity
        gy -= -intensity

        r, g, b = pixy[x - 1, y]
        gx += -2 * (r + g + b)

        r, g, b = pixy[x - 1, y + 1]
        gx += -(r + g + b)
        gy += (r + g + b)

        r, g, b = pixy[x, y - 1]
        gy += -2 * (r + g + b)

        r, g, b = pixy[x, y + 1]
        gy += 2 * (r + g + b)

        r, g, b = pixy[x + 1, y - 1]
        gx += (r + g + b)
        gy += -(r + g + b)

        r, g, b = pixy[x + 1, y]
        gx += 2 * (r + g + b)

        r, g, b = pixy[x + 1, y + 1]
        gx += (r + g + b)
        gy += (r + g + b)

        length = (gx * gx + gy * gy) ** 0.5

        length = int(length / 4328 * 255)

        pixy[x, y] = length, length, length

img.show()
