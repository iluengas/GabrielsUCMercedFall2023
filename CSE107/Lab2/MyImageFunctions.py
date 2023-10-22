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
    outputArray = np.zeros(shape=(_x, _y))

    #get the shape of the original image
    w, h = orig_im_pixels.shape 

    #Loop through each pixel in output array
    for i in range(_x+1):
        for j in range(_y+1):

            #calculate index mappings 
            x = (((i-0.5)/_x) * w) + 0.5
            y = (((j-0.5)/_y) * h) + 0.5

            #Implementation of bilinear interpolation: Derived from HW1 Prob5 pseudo 
                #Begin with conditional tree to determine 4 points that are closest to our mapped point on the original image

            #Check if mapping an int value -> will dictate how we set out two x-coords
            if (isinstance(x, int)):
                #set pixel value to interp mapping -1
                m1 = x - 1
                m2 = x - 1
            #If mapping is not an integer     
            else:
                #if mapping is less than 1
                if(x < 1):
                    m1 = 1 
                    m2 = 2
                #if mapping is greater than img width (-1 to adjust indexing)
                elif x > w - 1:
                    m1 = w-2
                    m2 = w - 1
                else:
                    m1 = math.floor(x) -1
                    m2 = math.ceil(x) -1

                #Same process as above -> will now dictate how we set out two y-coords
                if (isinstance(y, int)):
                    n1 = y -1
                    n2 =  y -1
                else: 
                    if(y < 1):
                        n1 = 1 
                        n2 = 2
                    elif y > h - 1:
                        n1 = h-2 
                        n2 = h - 1
                    else:
                        n1 = math.floor(y) - 1
                        n2 = math.ceil(y) - 1

                #Set our 4 point values to the values at the x/y indicies we just calculated for 
                p1 = (orig_im_pixels[m1][n1])
                p2 = (orig_im_pixels[m1][n2])
                p3 = (orig_im_pixels[m2][n1])
                p4 = (orig_im_pixels[m2][n2])

                #Solve for p5 using bilinear interpolation
                p5 = mybilinear(m1, n1, p1, m1, n2, p2, m2, n1, p3, m2, n2, p4, x - 1, y -1)

                #assign calculated P5 value into current pixel in output array (-1 to correct indexing)
                outputArray[i-1, j-1] = p5

    return outputArray


#Function to perform bilinear interpolation calculation to find value of pixel 
    #Parameters: Coordinates of 4 pixels we are using to interpolate as well as their color (p) values 
def mybilinear(x1, y1, p1, x2, y2, p2, x3, y3, p3, x4, y4, p4, x5, y5):
    #Calculate color value (interpolate) between two lower pixels 
    t1 = (p3 - p1)*((x5 - x1)/(x3 - x1)) + p1
    #Interpolate between two upper pixels 
    t2 = (p4 - p2)*((x5 - x2)/(x4 - x2)) + p2
    #interpolate between two prior interpolations to find p5 value 
    p5 = (t2 - t1)*((y5 - y1)/(y2 - y1)) + t1
    return p5



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