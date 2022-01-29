import cv2 as cv #imports opencv (cv2) called cv

#For image
# img = cv.imread('Photos/Cyberpunk.jpg') 

#For showing image
# cv.imshow('City', img)

#Normally takes an int. Int represents a camera for input(0 is for webcam, 1 is camera plugged in, etc)
#Can also take a path file for a video

#initializes the variable capture with a file path
# capture = cv.VideoCapture('Videos\Buildings.gif')
capture = cv.VideoCapture('Videos\Test.mp4')

#While loop to show frame by frame
while True:
    #reads frame by frame
    isTrue, frame = capture.read()
    #shows frame by frame
    cv.imshow('Video', frame)

    #If waitKey delay is 20 miliseconds and d key is pressed, video ends
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#realeases the path from capture
capture.release()
#destroys all the windows
cv.destroyAllWindows()

#Waits an infinite amount of time for a key press
# cv.waitKey(0)
