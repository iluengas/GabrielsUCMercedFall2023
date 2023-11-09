import numpy as np
import cv2 as cv

# Read the watertower image.
img = cv.imread('watertower.tif')

# Detect edges using the Canny edge detector.
edges = cv.Canny(img, 50, 150, apertureSize=3, L2gradient=True)

# Display the edge image and wait for a keypress.
cv.imshow("Edge Image", edges)
cv.waitKey(0)

# Save the image.
cv.imwrite('watertower_Canny_edges.tif', edges)