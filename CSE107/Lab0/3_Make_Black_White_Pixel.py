# Simple Python program to create black and white pixel in image and save the image.

# import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Import math for floor() function
import math

# Open a grayscale image from file.
im_gray = Image.open('puppy_grayscale.jpg')

# Use numpy to create a matrix with the pixel values.
im_gray_pixels = asarray(im_gray)

# Determine the dimensions of the image.
rows, cols = im_gray_pixels.shape
print("Image size is: ", rows, "rows x", cols, "columns")

# Make a copy of the matrix containing the pixels.
# First, create a new numpy matrix with the same size.
im_mod_pixels = np.zeros(shape=(rows, cols))

# Copy pixels from oringinal image to copy.
for row in range(rows):
    for col in range(cols):
        im_mod_pixels[row, col] = im_gray_pixels[row, col]

# Determine the location of the middle pixel. Use floor to ensure an integer.
middle_pixel_row = math.floor(rows/2)
middle_pixel_col = math.floor(cols/2)

# Create black pixel at this location.
im_mod_pixels[middle_pixel_row, middle_pixel_col] = 0;

# Create white pixel just to the right.
im_mod_pixels[middle_pixel_row, middle_pixel_col+1] = 255;

# Create image from img_mod_pixels matrix.
im_mod = Image.fromarray(np.uint8(im_mod_pixels))

# Display the modified image.
im_mod.show()

# Save the modified image to a jpg file. Lossy compression.
im_mod.save("puppy_gray_mod.jpg")

# Save the modified image to a tif file. Lossless compression.
im_mod.save("puppy_gray_mod.tif")
