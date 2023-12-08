import numpy as np
import math

def my_hough_transform(i_edge):
    print("Entered my_hough_transform")

    rows, cols = i_edge.shape

    #Get Diagonal
    diag = int(np.sqrt((rows*rows)+(cols*cols)))

    #Initialize accumulator array (Hough Space)
    accRows = (2 * (diag+1)) 
    accCols = 180
    accumulatorArray = np.zeros(shape = (accRows,accCols))

    #Iterate through each cell
    for row in range(rows):
        for col in range(cols):
            #if cell is an edge point
            if i_edge[row][col] == 255:
                #Begin iterating through possible theta values
                for theta in range(-89,90):
                    
                    #Convert Theta to radians
                    radians = np.deg2rad(theta)

                    #Compute rho
                    rho = round(col * math.cos(radians) + (row * math.sin(radians)))

                    #Adjust indexing and cast vote to accumulator array
                    accumulatorArray[int(rho+diag+1)][theta+90] += 1
        
    #Find max Value in accumulator array 
    theta_out = 0
    rho_out = 0
    rows, cols = accumulatorArray.shape
    maxVal = 0
    for row in range(rows):
        for col in range(cols):
            test = accumulatorArray[row][col]

            if test > maxVal:
                maxVal = test

                theta_out = col
                rho_out = row

    #Adjust indicies to get rho_out and theta_out for edge image
    rho_out = rho_out - diag - 1
    theta_out = theta_out - 90

    return theta_out, rho_out, accumulatorArray
