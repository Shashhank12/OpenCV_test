import cv2 as cv
from cv2 import resize
import numpy as np

frame = cv.imread('Photos/Cyberpunk.jpg')
resize = cv.resize(frame, (512,216))

lower_green = np.array([60, 125, 110])
upper_green = np.array([100, 255, 255])
frame_hsv = cv.cvtColor(resize, cv.COLOR_BGR2HSV)
frame_inrange = cv.inRange(frame_hsv, lower_green, upper_green)
cv.imshow('Camera Stream', frame_inrange)
cv.waitKey(0)
