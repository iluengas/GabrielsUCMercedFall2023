# Simple Python program to open image from a file, convert it to grayscale,
# display it, and save it to a file.

# import pillow
from PIL import Image, ImageOps

# open an image from file
im = Image.open('puppy.jpg')

# Convert image to gray scale.
im_gray = ImageOps.grayscale(im)

# Show the grayscale image.
im_gray.show()

# Save the grayscale image to file.
im_gray.save("puppy_grayscale.jpg")