from PIL import Image, ImageOps
                        #pill changes the organization of data - data types 
                        #numpy manipulates the image data itself -> greyscale, transformations, scaling 

im = Image.open("peanut.jpg")

im_gray = ImageOps.grayscale(im)

im_gray.show()