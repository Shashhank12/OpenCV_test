import cv2 as cv

img = cv.imread('Photos\Cyberpunk.jpg')
# cv.imshow('Cyberpunk', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blurs an image(src, must be odd numbers, what to blur)
blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade passing an image gives more detail and passing the blur reduces the edge detection details
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Edges', canny)

# Dilate an image. The lines are more thick
dilated = cv.dilate(canny, (7, 7), iterations = 3)
# cv.imshow('Dilated', dilated)

# Eroding an image(Features are more notiable and almost cancels out the dilated if parameters are the same)
eroded = cv.erode(dilated, (7, 7), iterations = 3)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (1024, 432))
cv.imshow('Resized', resized)

# Crop
cropped = img[50:400, 50:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)