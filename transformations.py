import cv2 as cv
from cv2 import ROTATE_90_CLOCKWISE
import numpy as np

img = cv.imread('Photos/Cyberpunk.jpg')

cv.imshow('Cyberpunk', img)

#translates an image
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
#translates based on the last two values(default is right[to go left, use negatives])
translated = translate(img, -100, -100)
# cv.imshow('Cyberpunk Translated', translated)

def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 0.5)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90, None)
# cv.imshow('Rotated', rotated)
#rotateUsingBuiltInCommand
rotateUsingBuiltIn = cv.rotate(img, rotateCode = ROTATE_90_CLOCKWISE)
# Flipping
    #0 = vertically, 1 = horizontally, -1 = both

resize = cv.resize(img, (512, 216))
cv.imshow('Resized', resize)
flip = cv.flip(resize, 1)
cv.imshow('Flip', flip)


cv.waitKey(0)