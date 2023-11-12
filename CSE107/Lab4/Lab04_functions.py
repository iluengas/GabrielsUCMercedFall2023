import numpy as np
from math import *

from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray


def spatial_filter( simple_image_pixels, impulse_filter_pixels):

    # The spatial filter applies the input filter to the input image and returns the result
    #
    # Syntax:  spatial_filter( simple_image_pixels, impulse_filter_pixels)
    #
    # Output: 
    #           filtered_image: 2D numpy array representing the image after applying spatial filter 
    # 
    # History: 
    #           Gabriel Benavidez       11/13/23                    

    m, n = simple_image_pixels.shape

    filtered_image = np.zeros(shape=(m, n))

    #Loops through each pixel and applies the spatial filter to find the new value for the pixel on the return image
    for row in range(m-1):
        for column in range(n-1):
            temp = simple_image_pixels[row-1][column-1] * impulse_filter_pixels[0][0] +\
                    simple_image_pixels[row-1][column] * impulse_filter_pixels[0][1] +\
                    simple_image_pixels[row-1][column+1] * impulse_filter_pixels[0][2] +\
                    simple_image_pixels[row][column-1] * impulse_filter_pixels[1][0] +\
                    simple_image_pixels[row][column] * impulse_filter_pixels[1][1] +\
                    simple_image_pixels[row][column+1] * impulse_filter_pixels[1][2] +\
                    simple_image_pixels[row+1][column-1] * impulse_filter_pixels[2][0] +\
                    simple_image_pixels[row+1][column] * impulse_filter_pixels[2][1] +\
                    simple_image_pixels[row+1][column+1] * impulse_filter_pixels[2][2]
            
            # print ('CHECK VAL'+ str(simple_image_pixels[row+1][column+1]))
            
            filtered_image[row][column] = temp

    return filtered_image

def gradient_magnitiude(input_img):

    # The gradient_magnitude function caclulates and returns the gradient magnitude of an input image 
    #
    # Syntax:  gradient_magnitiude(input_img)
    #
    # Output: 
    #           mag: the magnitude vector of the input image  
    # 
    # History: 
    #           Gabriel Benavidez       11/13/23 
    
    m, n = input_img.shape

    #Decalre and initialize both sobel filters 
    sobel1 = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    sobel2 = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

    #use the spatial_filter function to apply each sobel filter to the input image 
    sob1Img = spatial_filter(input_img, sobel1)
    sob2Img = spatial_filter(input_img, sobel2)

    mag=np.zeros(shape=(m,n))

    #Loop through each pixel in return image and calulcates the value using the two sobel filtered image
    for row in range (m-1):
        for col in range(n-1):
            mag[row][col] = sqrt((sob1Img[row][col])**2 + (sob2Img[row][col])**2)

    return mag

def find_edges(inputImg, threshold):

    # The find_edges function detects and outputs any hard edges found within an image (lines seperating color values) 
    #
    # Syntax:  find_edges(inputImg, threshold)
    #
    # Output: 
    #           edgesImg: the image marked with all edges found in the input image, only has 0 and 255 intensity pixelss
    # 
    # History: 
    #           Gabriel Benavidez       11/13/23 

    #Applies the gradient mag function to the input image
    gradient = gradient_magnitiude(inputImg)

    m, n = inputImg.shape 

    edgesImg = np.zeros(shape=(m, n))
    
    #Loops through each value in return image 
        #If pixel is below the threshold, it is converted to a black pixel 
            #If the pixel is above the threshold, it is converted to a solid white 255 pixel 
    for row in range(m-1):
        for col in range(n-1):
            if gradient[row][col] > threshold:
                edgesImg[row][col] = 255
            else:
                edgesImg[row][col] = 0

    return edgesImg

    





