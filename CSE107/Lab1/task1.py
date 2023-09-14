# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

#save image data to a variable 
img = Image.open('Beginnings.jpg')

# Show the image stored in variable
img.show()

#Calls grayscale operation with image variable argument -> returns black and white version of image argument
img_gray = ImageOps.grayscale(img)

img_gray.show()

#calls asarray function with image argument -> returns numpyMatrix representing image
numpyMatrixImage = asarray(img_gray)

#use .shape method to save dimensions of array to rows and columns variable 
rows, columns = numpyMatrixImage.shape

#current max variable declared and defined with int value 0
#for loop iterating up to the value of row, nested iteration up to the value of columns for each row iteration 
    #For each iteration, x/y are used to find value index the np matrix 
    #if the value found at the index is larger than currentMax, currentMax is updated with the new value 
#currentMax is printed at the end of the loop 
currentMax = 0

for x in range(rows):
    for y in range(columns):
        if (currentMax < numpyMatrixImage[x][y]):
            currentMax = numpyMatrixImage[x][y]
        else:
            continue
        #print("[" + x + "]" + "[" + y +"] = " + numpyMatrixImage[x][y])

print("Max value of Beginnings_grayscale: " + str(currentMax))

#New np matrix is delcared, number of rows is set to # of columns in numpyMatrixImage, # of coulmns is set to # of rows from same matrix. 
#for loop iterating up to the value of row, nested iteration up to the value of columns for each row iteration 
    #at every index in numpyMatrixImage, that index value is copied to the new np matrix rot90Matrix starting from right to left, top down 
        #(numpyMatrixImage is read left-to-right, then top-down), then copied to rot90Matrix top-down, then left-to-right 
rot90CC = np.zeros(shape=(columns, rows))

for x in range(rows):
    for y in range(columns):
        rot90CC[y][x] = numpyMatrixImage[x][y]

#Convert np array to an image using Pillow method and display image with .show()
image = Image.fromarray(rot90CC)
image = image.convert("L") #convert created image to grayscale mode to allow us to save 
image.save("rot90CC.jpg")
image.show()


#Same array initialization and iteration as preceeding loop
    #instead of reading numpyMatrixImage left-to-right, then top-down) and copying to rot90Matrix top-down, then left-to-right 
        #rot90ClockWise is copied to bottom-up, then right-to-left starting at the last index in the column/row 
rot90ClockWise = np.zeros(shape=(columns, rows))

for x in range(rows):
    for y in range(columns):
        rot90ClockWise[(columns-1) -y][(rows-1) - x] = numpyMatrixImage[x][y]

#Convert np array to an image using Pillow method and display image with .show()
image = Image.fromarray(rot90ClockWise)
image = image.convert("L")
image.save("rot90ClockWise.jpg")
image.show()


#same process as currentMax loop for Beginnings_grasyscale
    #we are now reading from rot90Clockwise indices to find currentMax
currentMax = 0

for x in range(rows):
    for y in range(columns):
        if (currentMax < rot90ClockWise[y][x]):
            currentMax = rot90ClockWise[y][x]
        else:
            continue
        #print("[" + x + "]" + "[" + y +"] = " + numpyMatrixImage[x][y])

print("Max value of rot90ClockWise: " + str(currentMax))


