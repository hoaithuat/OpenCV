import numpy as np
import cv2 as cv

img1 = cv.imread('pic1.png', cv.IMREAD_GRAYSCALE)
height = len(img1)
width  = len(img1[0])
filterSize =3
temp = []
indexer = filterSize//2
img2 = np.empty_like(img1)
for i in range(height):
    for j in range(width):
        for rowKernel in range(filterSize):
            if i+rowKernel-indexer < 0 or i+rowKernel-indexer > height-1:
                for col1 in range(filterSize):
                    temp.append(0)
            elif j+rowKernel-indexer < 0 or j+indexer+rowKernel > width-1:
                for col2 in range(filterSize):
                    temp.append(0)
            else:
                for col3 in range(filterSize):
                    temp.append(img1[i+rowKernel-indexer][j+col3-indexer])
        temp.sort()
        img2[i][j] = temp[len(temp)//2]
        temp = []

cv.imshow('input', img1)
cv.imshow('output', img2)

cv.waitKey(0)
cv.destroyAllWindows()
