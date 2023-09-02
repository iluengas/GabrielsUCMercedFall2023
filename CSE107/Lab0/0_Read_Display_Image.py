# Simple Python program to open image from a file and display it.

# import pillow
from PIL import Image

# open an image from file
im = Image.open('puppy.jpg')

# show the image
im.show()