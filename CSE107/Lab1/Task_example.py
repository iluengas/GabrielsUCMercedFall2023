# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

# Read the image from file.
im = Image.open('Beginnings.jpg')

# Show the image.
im.show()

# Convert image to gray scale.
im_gray = ImageOps.grayscale(im)

# Show the grayscale image.
im_gray.show()

# Get access to the pixel values through the matrix im_gray_pixels.
im_gray_pixels = asarray(im_gray)

# Determine the dimensions of the image.
rows, cols = im_gray_pixels.shape
print("Image size is: ", rows, "rows x", cols, "columns")

# Create a new matrix this is 40 pixels smaller along each dimension.
crop_rows = rows - 40
crop_cols = cols - 40
im_gray_crop_pixels = np.zeros(shape=(crop_rows, crop_cols))

# Copy values from center of original matrix to smaller matrix. Ignore band of 20 pixels.
for row in range(20, rows-20):
    for col in range(20, cols-20):
        im_gray_crop_pixels[row-20, col-20] = im_gray_pixels[row, col]

# Create an image from im_gray_crop_pixels.
im_gray_crop = Image.fromarray(np.uint8(im_gray_crop_pixels))

# Display the image.
im_gray_crop.show()

# Save the image.
im_gray_crop.save("Beginnings_grayscale_crop.jpg")

