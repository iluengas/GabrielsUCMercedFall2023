# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

###############################################################################
# Detect edges in a simple image.
###############################################################################

# Create a simple image with black (0) on the left half and white (255) on the right half.
simple_image_pixels = np.zeros(shape=(100, 100))
simple_image_pixels[:,50:99] = 255

# Display the simple image.
simple_image = Image.fromarray(np.uint8(simple_image_pixels))
simple_image.show()

# Import spatial_filter from Lab04_functions.
from Lab04_functions import find_edges

# Perform edge detection by thresholing the gradient magnitude.
threshold = 200
edge_image_pixels = find_edges( simple_image_pixels, threshold )

# Create an image from numpy matrix edge_image_pixels.
edge_image = Image.fromarray(np.uint8(edge_image_pixels.round()))

# Show the edge image.
edge_image.show()

# Save the edge image.
edge_image.save( 'simple_image_edges.tif' )

###############################################################################
# Detect edges in the watertower image.
###############################################################################

# Read the watertower image from file.
lab_image = Image.open('watertower.tif')

# Show the image.
lab_image.show()

# Create numpy matrix to access the pixel values.
# NOTE THAT WE WE ARE CREATING A FLOAT32 ARRAY SINCE WE WILL BE DOING
# FLOATING POINT OPERATIONS IN THIS LAB.
lab_image_pixels = asarray(lab_image, dtype=np.float32)

# Perform edge detection by thresholing the gradient magnitude.
threshold = 200
edge_image_pixels = find_edges( lab_image_pixels, threshold )

# Create an image from numpy matrix edge_image_pixels.
edge_image = Image.fromarray(np.uint8(edge_image_pixels.round()))

# Show the edge image.
edge_image.show()

# Save the edge image.
edge_image.save( 'watertower_edges.tif' )