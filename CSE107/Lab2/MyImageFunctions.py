import numpy as np
import math

#main resizing function:
    #Takes in image, new width and height, and interpolation mode string
def myImageResize(orig_im_pixels, x, y, mode):

    #Switch case for mode string to determine which interpolation algorithm to use
    if mode == "nearest":
        #this case will return the image resized with nearest neighbor interpolation
        print("Begin Nearest Neighbor")
        return nearestNeighborInterpolation(orig_im_pixels, x, y)
    elif mode == 'bilinear':
        #This case will return image resized with bilinear interpolation
        print("Begin bilnear")
        return bilinearInterpolation(orig_im_pixels, x, y)
    else:
        #Error handling - unkown mode string
        print("ERROR - Mode not defined")

#Nearest Neighbor interpolation function:
    #Takes in original image, and new width/height 
def nearestNeighborInterpolation(orig_im_pixels, _x, _y):
    print("Entered NN")
    #Initialize the output array with 0s, width and height are set to new values
    outputArray = np.zeros(shape=[_x, _y])

    #get the shape of the original image
    w, h = orig_im_pixels.shape 

    #Get scaling factors between the two images
    xScale = _x/(w-1)
    yScale = _y/(h-1)

    #interate through each pixel in output array (-1 to shape) to correct indexing
    for x in range(_x-1): 
        for y in range(_y-1): 

            #Current pixel in output array is set to the value of the pixel with x/y closest to (current pixel * scaling factor), +1 to correct indexing  
            outputArray[x + 1, y + 1]= orig_im_pixels[1 + int(x/xScale), 1 + int(y/yScale)] 

    return outputArray

def bilinearInterpolation(orig_im_pixels, _x, _y):
    print("Entered BL")

    #Initialize the output array with 0s, width and height are set to new values
    outputArray = np.zeros(shape=[_x, _y])

    #get the shape of the original image
    w, h = orig_im_pixels.shape 

    #Get scaling factors between the two images
    xScale = _x/(w-1)
    yScale = _y/(h-1)

    #interate through each pixel in output array (-1 to shape) to correct indexing
    for i in range(_x-1): 
        for j in range(_y-1): 
            #get approximations for mapped values on original image
            x = i*xScale
            y = j*yScale

            x_floor = math.floor(x)
            x_ceil = min(w-1, math.ceil(x))
            y_floor = math.floor(y)
            y_ceil = min(h-1, math.ceil(y))

            v1 = orig_im_pixels[x_floor, y_floor]
            v2 = orig_im_pixels[x_ceil, y_floor]
            v3 = orig_im_pixels[x_floor, y_ceil]
            v4 = orig_im_pixels[x_ceil, y_ceil]

            q1 = v1 * (x_ceil - x) + v2 * (x - x_floor)
            q2 = v3 * (x_ceil - x) + v4 * (x - x_floor)
            q = q1 * (y_ceil - y) + q2 * (y - y_floor)
            outputArray[i,j] = q
                    




    return outputArray


#Function to perform a Root Mean Square Error calculation between the np.arrays of two images:
    #Parameters: original image, image to make calculations against
def myRMSE(origMat, alteredMat):
    
    #Conditional to ensure two images have the same dimensions 
    if (origMat.shape != alteredMat.shape):
        print("ERROR - img sizes do not match")
        return 0
    
    #Get the shape(will be shape of both images)
    w, h = origMat.shape 

    #TypeCast values in both arrays se we can perform valculations
        #Find difference between two matrices squared
            #Get the sum of the difference matrix
    RMSE = np.sum((origMat.astype('float') - alteredMat.astype('float'))**2)

    #Divide value by the product of the dimensions 
        #squre root the quotient
    RMSE = math.sqrt(RMSE/float(w*h))

    #return the calculated RMSE value 
    return RMSE