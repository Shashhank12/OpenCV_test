import cv2 as cv
import numpy as np

imgInitial = cv.imread('Photos/Cyberpunk.jpg')
img = cv.resize(imgInitial, (1024, 432))

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

cv.imshow('Cyber', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# Method to find the edges of an image
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Contours is a python list of all the coordinates found in an image
# Hierarchy(if there is a square inside a square)
# the first is the src, the second param is what how it finds contour methods. Retr list returns all
# The CHAIN_APPROX is helpful return only the important

# If the intensity is bellow 125, it is set to black and if it above 255, then it is set to white
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Returns the contours and the hierarchies. It gets the image from thres and uses no chain approx. Contours are almost like edges but not exactly. They are like where the edges connect
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# Prints out how many contours there are
print(len(contours))

# Draws contours on a blank window in the color red
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("contours", blank)

cv.waitKey(0)