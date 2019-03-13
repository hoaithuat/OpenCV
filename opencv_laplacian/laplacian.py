import cv2 as cv 
import numpy as np 

img = cv.imread('pic1.png',cv.IMREAD_GRAYSCALE)
ddept = cv.CV_16S
kerrne_size = 3
img2 = cv.Laplacian(img,ddept,kerrne_size)
abs_img2 = cv.convertScaleAbs(img2)
img3 = img - abs_img2

cv.imshow('input',img)
cv.imshow('output1',abs_img2)
cv.imshow('output2',img3)

cv.waitKey(0)
cv.destroyAllWindows()  