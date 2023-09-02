# Simple Python program to create 100x100 pixel grayscale image, display, and save.

# import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Import random for randomint() function
import random

# Use numpy to create a 100x100 pixel image with all zeros.
n_rows = 100
n_cols = 100
im_pixels = np.zeros(shape=(n_rows, n_cols))

# Loop through each pixel and assign random value from 0 to 255 (inclusive).
for row in range(n_rows):
    for col in range(n_cols):
        im_pixels[row, col] = random.randint(0, 255)

# Create image from img_pixels matrix.
im = Image.fromarray(np.uint8(im_pixels))

# Display the image.
im.show()

# Save the image to a tif file. Lossless compression.
im.save("random_image.tif")
