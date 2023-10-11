import numpy as np
import math

def myImageResize(orig_im_pixels, x, y, mode):
    print("imResize")

    if mode == "nearest":
        print("Begin Nearest Neighbor")
        return nearestNeighborInterpolation(orig_im_pixels, x, y)
    elif mode == 'bilinear':
        print("Begin bilnear")
        return bilinearInterpolation(orig_im_pixels, x, y)
    else:
        print("ERROR - Mode not defined")

def nearestNeighborInterpolation(orig_im_pixels, sx, sy):
    print("Entered NN")
    outputArray = np.zeros(shape=[sx, sy])
    w, h = orig_im_pixels.shape 

    xScale = sx/(w-1)
    yScale = sy/(h-1)

    for x in range(sx-1): 
        for y in range(sy-1): 
            outputArray[x + 1, y + 1]= orig_im_pixels[1 + int(x/xScale), 1 + int(y/yScale)] 

    return outputArray

def bilinearInterpolation(orig_im_pixels, x, y):
    print("Entered BL")
    return orig_im_pixels

def myRMSE(origMat, alteredMat):
    
    if (origMat.shape != alteredMat.shape):
        print("ERROR - img sizes do not match")
    else:
        print("Fine")

    return 3