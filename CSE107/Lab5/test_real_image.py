# Test script for detecting the most prominent line in an image using the Hough transform.

# Import pillow
from PIL import Image

# Import numpy
import numpy as np
from numpy import asarray

# Import openCV
import cv2 as cv

# Read the runway image.
in_image = Image.open('runway_image.tif')

# Show the image.
in_image.show()

# Create numpy matrix to access the pixel values.
in_image_pixels = asarray(in_image)

# Detect edges using the Canny edge detector.
edge_image_pixels = cv.Canny(in_image_pixels, 50, 100, apertureSize=3, L2gradient=True)

# Create an image to display and save.
edge_image = Image.fromarray(np.uint8(edge_image_pixels.round()))

# Show the edge image.
edge_image.show()

# Save the edge image.
edge_image.save('runway_image_edge.tif')

# Import my_hough_transform
from my_hough_transform import my_hough_transform

# Find (most prominent) line using Hough transform.
theta_est, rho_est, accumulator = my_hough_transform( edge_image_pixels )

# Report estimated line parameters.
print( 'estimated theta = ', theta_est,' estimated rho = ', rho_est )

# Import draw_line_on_image
from Lab05_Functions import draw_line_on_image

# Draw the detected line on the runway image.
in_image_pixels_copy = np.copy(in_image_pixels)
image_with_line_pixels = draw_line_on_image( in_image_pixels_copy, theta_est, rho_est )

# Create an image to display and save.
image_with_line = Image.fromarray(np.uint8(image_with_line_pixels.round()))

# Show the image.
image_with_line.show()

# Save the image.
image_with_line.save('runway_image_with_line.tif')

# Compute log of accumulator matrix because its dynamic range is typically
# too large to visualize details.
accumulator_log = np.log( accumulator + 1 )

# Scale it to [0,255].
accumulator_log = 255 * (accumulator_log / np.max(accumulator_log))

# View log of accumulator.
accumulator_log_image = Image.fromarray(np.uint8(accumulator_log))
accumulator_log_image.show()

# Write image to file.
accumulator_log_image.save( 'runway_image_accumulator.tif' )

