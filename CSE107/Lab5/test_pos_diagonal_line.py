# Import pillow
from PIL import Image

# Import numpy
import numpy as np
from numpy import asarray

# Import math Library
import math

# Import draw_line_on_image
from Lab05_Functions import draw_line_on_image

# Test script for detecting a a diagonal line with a positive theta angle
# in an image using the Hough transform.

# Create a blank image (matrix of zeros).
size_x = 100;
size_y = 100;
blank_image_pixels = np.zeros(shape=(size_x, size_y))

# Draw a diagonal line though middle of image. Specify line
# using normal form: theta=45 (degrees), rho=half diagonal size. This line
# image is what we would get from edge detection as it only has two values,
# edge=255 and non-edge=0.
theta_true = 45
rho_true = round( 0.5 * math.sqrt( size_x * size_x + size_y * size_y ) )
image_with_line_pixels = draw_line_on_image( blank_image_pixels, theta_true, rho_true )

# Display the image with the line.
image_with_line = Image.fromarray(np.uint8(image_with_line_pixels))
image_with_line.show()

# Write image to file.
image_with_line.save( 'pos_diagonal_line.tif' )

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
accumulator_log_image.save( 'pos_diagonal_line_accumulator.tif' )