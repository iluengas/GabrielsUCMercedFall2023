from PIL import Image, ImageOps

# Import numpy and custom library myImageFunctions
import numpy as np

#Create new 0 array with dimensions 100x256
gsImage = np.zeros(shape=(100,256))

#initialize total variable to 0
total = 0
#iterate through each column in each row of the array 
    #set the value of the index to the current column index (0-255 colorScale, 0-255 columns to be linearly filled in)
    #update the total with value of the column index
for x in range(100):
    for y in range(256):
        gsImage[x][y] = y
        total = total+y

#Print the average pixel value of the gradient image - divide total by number of indicies
print ("Average Pixel Value: " + str(total/(100*256)))
#Convert gsImage to an image
img = Image.fromarray(gsImage)

#show image to screen
img.show()

img.convert("L") #convert created image to grayscale mode to allow us to save 

#save inverted .tif image to file
img.save("gradient.tif")