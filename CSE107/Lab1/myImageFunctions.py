import numpy as np

def myImageInverse (inputArray):
    #save row/column #s of input Array to variables 
    rows, columns = inputArray.shape
    #print (str(rows) + " " + str(columns))

    #initialize a new array with the same dimensions as input array and fill with zeros
    outputArray = np.zeros(shape=(rows,columns))

    #iterate through each row and column of input matrix
        #on each iteration, subtract each pixel value of the inputArray index from 255 (giving the inverse of the pixel value as 255 is max)
        #save this new value to the same index in the outputArray
    #return outputArray
    max = 0
    for x in range(rows):
        for y in range(columns):
            outputArray[x][y] = 255-inputArray[x][y]
            if (max < 255-inputArray[x][y]):
                max = 255-inputArray[x][y]
    print (str(max))
    return outputArray

