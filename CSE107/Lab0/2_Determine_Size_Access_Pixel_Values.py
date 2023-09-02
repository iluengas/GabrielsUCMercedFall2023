# Simple Python program to determine image size and show values of four corner pixels.

# import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Open a grayscale image from file.
im_gray = Image.open('puppy_grayscale.jpg')

# Use numpy to create a matrix with the pixel values.
im_gray_pixels = asarray(im_gray)

# Determine the dimensions of the image.
rows, cols = im_gray_pixels.shape
print("Image size is: ", rows, "rows x", cols, "columns")

# Get value of top left pixel (should be 228).
top_left_value = im_gray_pixels[0][0]
print("Top left pixel has value: ", top_left_value)

# Get value of top right pixel (should be 158).
top_right_value = im_gray_pixels[0, cols-1]
print("Top right pixel has value: ", top_right_value)

# Get value of bottom left pixel (should be 114).
bottom_left_value = im_gray_pixels[rows-1, 0]
print("Bottom left pixel has value: ", bottom_left_value)

# Get value of bottom right pixel (should be 88).
bottom_right_value = im_gray_pixels[rows-1, cols-1]
print("Bottom right pixel has value: ", bottom_right_value)
