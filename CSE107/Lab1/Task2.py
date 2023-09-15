from PIL import Image, ImageOps

# Import numpy and custom library myImageFunctions
import numpy as np
import myImageFunctions as mif

#load in image to a variable
img = Image.open('Watertower.tif')

#Print the mode to verify grayscale image
print("image mode is:", img.mode)

# Show the image stored in variable
img.show()

#convert image to nparray
arr1 = np.asarray(img)

#call function from myImageFunctions to invert the image 
inverseArr1 = mif.myImageInverse(arr1)

#create grayscale image from array
inverseImg = Image.fromarray(inverseArr1)

#Show the image
inverseImg.show()

inverseImg.convert("L") #convert created image to grayscale mode to allow us to save 

#save inverted .tif image to file
inverseImg.save("inverseWatertower.tif")