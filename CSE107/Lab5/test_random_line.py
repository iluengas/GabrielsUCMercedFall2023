# Import pillow
from PIL import Image

# Import numpy
import numpy as np
from numpy import asarray

# Import math Library
import math

# Import random to generate random theta and rho values
import random

# Import draw_line_on_image
from Lab05_Functions import draw_line_on_image

# Test script for detecting a randomly oriented line in an image using the
# Hough transform.

# Create a blank image (matrix of zeros).
size_x = 100;
size_y = 100;
blank_image_pixels = np.zeros(shape=(size_x, size_y))

# Diagonal size of image.
size_d = math.floor(math.sqrt( size_x * size_x + size_y * size_y ))

# Can't detect lines that have too few edge points (i.e., ones that only
# pass through the corner of an image) or ones that don't even cross the
# image. So, set a threshold that the line should constitute 20 percent of
# diagonal size of image.
percent_edge_points = 0.2

# Draw a randomly oriented line through the image.
# Keep creating sample images until enough of the line appears in the image
# for the Hough transform to work.
num_edge_pixels = 0;
while num_edge_pixels < (percent_edge_points * size_d):

    # Zero out array.
    blank_image_pixels.fill(0)

    # Compute random theta from -89 to 90 inclusive.
    theta_true = random.randint(-89, 90)

    # Compute random rho from -size_d to size_d. Note, though, that many of
    # these lines will not actually cross the image. Thus the test for a
    # line of minimum length.
    rho_true = random.randint(-size_d, size_d)

    image_with_line_pixels = draw_line_on_image( blank_image_pixels, theta_true, rho_true )

    # Count the number of edge pixels.
    num_edge_pixels = np.count_nonzero(image_with_line_pixels)

# Display the image with the line.
image_with_line = Image.fromarray(np.uint8(image_with_line_pixels))
image_with_line.show()

# Write image to file.
image_with_line.save( 'random_line.tif' )

# Import my_hough_transform
from my_hough_transform import my_hough_transform

# Find (most prominent) line using Hough transform.
theta_est, rho_est, accumulator = my_hough_transform( image_with_line_pixels )

# Report true and estimated line parameters.
print( 'true theta = ', theta_true,' true rho = ', rho_true )
print( 'estimated theta = ', theta_est,' estimated rho = ', rho_est )

# Compute log of accumulator matrix because its dynamic range is typically
# too large to visualize details.
accumulator_log = np.log( accumulator + 1 )

# Scale it to [0,255].
accumulator_log = 255 * (accumulator_log / np.max(accumulator_log))

# View log of accumulator.
accumulator_log_image = Image.fromarray(np.uint8(accumulator_log))
accumulator_log_image.show()

# Write image to file.
accumulator_log_image.save( 'random_line_accumulator.tif' )
