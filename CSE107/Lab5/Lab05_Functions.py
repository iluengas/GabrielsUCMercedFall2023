# Lab05_functions.py

# Import numpy
import numpy as np

# Import math Library
import math

def draw_line_on_image( image_in_pixels, theta, rho ):

    # draw_line_on_image  Draw a line on an image. The line is specified using
    # the theta and rho parameters of its normal form. The pixels corresponding
    # to the line are set to 255. The other pixels are not touched. The input
    # should be a grayscale image (numpy matrix of pixels).
    #
    # Syntax:
    #   image_out = draw_line_on_image( image_in_pixels, theta, rho )
    #
    # Input:
    #   in_image = The grayscale image on which to draw the line. Type: numpy array
    #   theta = The angle of the line in degrees. Horizonal is 0.
    #   rho = The length of the perpendicular bisector in pixels.
    #
    # Output:
    #   image_out_pixels = The image with the line drawn. Type: numpy array
    #
    # History:
    #   S. Newsam     11/25/2023   created

    # Determine the dimensions of the input image.
    size_x, size_y = image_in_pixels.shape

    # If theta is between -45 and 45, vary y.
    if abs(theta) <= 45:
        # Convert theta to radians since math.sin and math.cos expect radians.
        theta_radians = math.radians(theta)
        # Range over all values of y in image.
        for y in range(size_y):
            # Determine x location of line point using normal form.
            x = round(((rho-1) - (y * math.sin(theta_radians))) / math.cos(theta_radians))
            if (0 <= x) & (x <= size_x - 1):
                # Write line point.
                image_in_pixels[x, y] = 255
    
    # If theta is not between 45 and 45, vary x.
    else:
        # Convert theta to radians since math.sin and math.cos expect radians.
        theta_radians = math.radians(theta)
        # Range over all values of x in image.
        for x in range(size_x):
            # Determine y location of line point using normal form.
            y = round( ((rho-1) - (x * math.cos(theta_radians))) / math.sin(theta_radians) )
            # Make sure not off edge of image.
            if (0 <= y) & (y <= size_y - 1):
                # Write line point.
                image_in_pixels[x, y] = 255

    return image_in_pixels

