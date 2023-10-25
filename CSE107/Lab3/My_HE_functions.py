# MyHEFunctions.py

# Import numpy
import numpy as np

def compute_histogram( image_pixels ):

    #Decalre histogram Vector for our pixel values
    hist = np.zeros(shape=(256))

    #Get array shape 
    m, n = image_pixels.shape

    #Loop through each pixel in image_pixels
    for x in range(m):
        for y in range(n):
            #Get the pixel intensity value and increment the corresponding bin in our histogram
            # Normalized histogram with psuedo from Lect 13 -> hist now will show probalility of occurance rather than count
            hist[int(image_pixels[x][y])] += (1/(m*n))

    return hist


def equalize( in_image_pixels ):

    normalizedHist = compute_histogram(in_image_pixels)

    
    #Decalre tranformation Vector for our pixel values
    transformationVect = np.zeros(shape=(256))

    for x in range(normalizedHist):
        transformationVect[x] = (x*)

# <your function header>

# <your implementation>
    return 


def plot_histogram( hist ):
    # plot_histgram  Plots the length 256 numpy vector representing the normalized
    # histogram of a grayscale image.
    #
    # Syntax:
    #   plot_histogram( hist )
    #
    # Input:
    #   hist = The length 256 histogram vector..
    #
    # Output:
    #   none
    #
    # History:
    #   S. Newsam     10/15/2023   created

    # Import plotting functions from matplotlib.
    import matplotlib.pyplot as plt

    plt.bar( range(256), hist )

    plt.xlabel('intensity value')

    plt.ylabel('PMF'); 

    plt.show()
