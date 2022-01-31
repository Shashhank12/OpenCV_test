import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow('Blank', blank)

# Paint the image a certain color
# blank[0:100, 1:200] = 0, 255, 0
# blank[100:200, 1:200] = 255, 0, 0
# blank[200:300, 1:200] = 255, 0, 255
# blank[300:400, 1:200] = 255, 255, 0
# blank[400:500, 1:200] = 255, 255, 255
# cv.imshow('Green', blank)

# Draw a Rectangle
    #Draws a rectangle(start point, endpoint, color, thickness [-1 is fill fully])
        # cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness = 1)
#Draws a rectangle(start point, endpoint, color, filled fully)       
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), cv.FILLED)
# #Draws a rectangle with half the size of a normal
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = -1)
# cv.imshow('Rectangle', blank)

#Draw a circle first(which image, center, radius, color, thickness)
# cv.circle(blank, (250, 250), 40, (0, 255, 255), thickness = -1)
# cv.imshow('Circle', blank)

#Draw a line
# cv.line(blank, (0, 0), (500, 500) , (255, 255, 255), thickness = 4)
# cv.imshow('Line', blank)

#Write text
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 255), thickness = 1)
cv.imshow('Text', blank)


cv.waitKey(0)