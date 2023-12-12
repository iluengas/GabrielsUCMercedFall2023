import numpy as np
import math
    # Applies Hough Transform to edge image
    #
    # Syntax:   my_hough_transform(i_edge)
    #
    # Output: 
    #           rho, theta, accumulator matrix from Hough transform algorithm
    # 
    # History: 
    #           Gabriel Benavidez       11/13/23    
def my_hough_transform(i_edge):
    print("Entered my_hough_transform")

    rows, cols = i_edge.shape

    #Get Diagonal
    diag = (np.sqrt((rows*rows)+(cols*cols)))

    #Initialize accumulator array (Hough Space)
    accRows = int((2 * diag+1)) 
    accCols = 180
    accumulatorArray = np.zeros(shape = (accRows,accCols))
    

    #create Index array for rho values
    degreeIndex = np.zeros(accRows)

    #Populate Index array 
    for i in range(1, accRows + 1):
        degreeIndex[i - 1] = int(-diag + i - 1)


    #Iterate through each cell
    for row in range(rows):
        for col in range(cols):
            #if cell is an edge point
            if i_edge[row][col] == 255:
                #Begin iterating through possible theta values
                for theta in range(-89, 90):
                    
                    #Convert Theta to radians
                    radians = np.deg2rad(theta)

                    #Compute rho
                    rho = (row * math.cos(radians)) + (col * math.sin(radians))

                    #find closest value in degreeIndex to calculated rho value
                    min_difference = diag
                    for i in range(len(degreeIndex)):
                        difference = abs(degreeIndex[i] - rho)
                        if difference < min_difference:
                            min_difference = difference
                            ind = i


                    #Adjust indexing and cast vote to accumulator array
                    # accumulatorArray[int((rho)+diag+1)][theta+90] += 1
                    accumulatorArray[int(ind)][int(theta+89)] += 1
        

    #Find rho and theta 
    maxVal = 0
    theta_out = None
    rho_out = None
    for row in range(accRows):
        for col in range(accCols):
            if (accumulatorArray[row][col] > maxVal):
                maxVal = accumulatorArray[row][col]

                #Adjust for appropriate indexing 
                theta_out = col - 89
                rho_out = row - int(diag)
    
                    


    return theta_out, rho_out, accumulatorArray
    