import cv2 as cv 
import numpy as np 

img = cv.imread('pic1.png',cv.IMREAD_GRAYSCALE)
img2 = cv.blur(img,(5,5))

cv.imshow('input',img)
cv.imshow('Output',img2)

cv.waitKey(0)
cv.destroyAllWindows()
