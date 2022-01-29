import cv2 as cv #imports opencv (cv2) called cv

#For image
# img = cv.imread('Photos/Cyberpunk.jpg') 

#For showing image
# cv.imshow('City', img)

#Normally takes an int. Int represents a camera for input(0 is for webcam, 1 is camera plugged in, etc)
#Can also take a path file for a video

capture = cv.VideoCapture('Videos/Buildings.gif')

while True:
    isTrue, frame = capture.read()

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#Waits an infinite amount of time for a key press
# cv.waitKey(0)
