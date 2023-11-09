# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

###############################################################################
# Create a simple image and filter it with an "impulse" filter which shouldn't change it.
###############################################################################

# Create a simple image with black (0) on the left half and white (255) on the right half.
simple_image_pixels = np.zeros(shape=(100, 100))
simple_image_pixels[:,50:99] = 255

# Display the simple image.
simple_image = Image.fromarray(np.uint8(simple_image_pixels))
simple_image.show()

# Create an "impulse" filter which has all zeros except for the middle entry.
impulse_filter_pixels = np.zeros(shape=(3, 3))
impulse_filter_pixels[1][1] = 1

# Import spatial_filter from Lab04_functions.
from Lab04_functions import spatial_filter

# Apply impulse filter to simple image.
filtered_image_pixels = spatial_filter( simple_image_pixels, impulse_filter_pixels)

# Create an image from numpy matrix filtered_image_pixels.
filtered_image = Image.fromarray(np.uint8(filtered_image_pixels.round()))

# Show the filtered image. This should be the same as the unfiltered simple image.
filtered_image.show()

###############################################################################
# Filter the simple image with an averaging filter which should smooth it.
###############################################################################

# Create a 3x3 averaging filters with all values equal to 1/9.
averaging_filter_pixels = np.zeros(shape=(3, 3))
for row in range(3):
    for col in range(3):
        averaging_filter_pixels[row][col] = 1/9

# Apply filter to image.
filtered_image_pixels = spatial_filter( simple_image_pixels, averaging_filter_pixels)

# Create an image from numpy matrix filtered_image_pixels.
filtered_image = Image.fromarray(np.uint8(filtered_image_pixels.round()))

# Show the filtered image.
filtered_image.show()

# Save the smoothed simple image.
filtered_image.save( 'simple_image_smoothed.tif' )

###############################################################################
# Filter the watertower image with the "impulse" filter which shouldn't change it.
###############################################################################

# Read the lab image from file.
lab_image = Image.open('watertower.tif')

# Show the image.
lab_image.show()

# Create numpy matrix to access the pixel values.
# NOTE THAT WE WE ARE CREATING A FLOAT32 ARRAY SINCE WE WILL BE DOING
# FLOATING POINT OPERATIONS IN THIS LAB.
lab_image_pixels = asarray(lab_image, dtype=np.float32)

# Apply impulse filter to simple image.
filtered_image_pixels = spatial_filter( lab_image_pixels, impulse_filter_pixels)

# Create an image from numpy matrix filtered_image_pixels.
filtered_image = Image.fromarray(np.uint8(filtered_image_pixels.round()))

# Show the filtered image. This should be the same as the unfiltered watertower image.
filtered_image.show()

###############################################################################
# Filter the watertower image with an averaging filter which should smooth it.
###############################################################################

# Apply impulse filter to simple image.
filtered_image_pixels = spatial_filter( lab_image_pixels, averaging_filter_pixels)

# Create an image from numpy matrix filtered_image_pixels.
filtered_image = Image.fromarray(np.uint8(filtered_image_pixels.round()))

# Show the filtered image. This should be the same as the unfiltered watertower image.
filtered_image.show()

# Save the smoothed watertower image.
filtered_image.save( 'watertower_smoothed.tif' )
