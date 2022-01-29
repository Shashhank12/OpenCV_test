import cv2 as cv #imports opencv (cv2) called cv

img = cv.imread('Photos/Cyberpunk.jpg') 

cv.imshow('City', img)

cv.waitKey(0)