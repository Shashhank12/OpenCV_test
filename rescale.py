import cv2 as cv

 
#Creates a function(method) that rescales a frame to 0.75% of its original
def rescaleFrame(frame, scale = 0.75):
    #sets the variable width to the scaled width
    width = int(frame.shape[1] * scale)
    #sets the variable width to the scaled with
    height = int(frame.shape[0] * scale)
    #initializes the dimenstions
    dimensions = (width, height)
    #returns the image, with the scaled dimensions and also with a INTER_AREA compression(moire-free compresion)
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

img = cv.imread('Photos/Cyberpunk.jpg')
cv.imshow('Cyberpunk', img)
 
pic_resize = rescaleFrame(img)
cv.imshow('Cyberpunk Resized', img)

capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)


    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()