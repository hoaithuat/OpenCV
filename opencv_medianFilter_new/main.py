import numpy as np
import cv2 as cv



img1 = cv.imread('pic1.png', cv.IMREAD_GRAYSCALE)
height = len(img1)
width  = len(img1[0])
filterSize =3
temp = []
indexer = filterSize//2
img2 = np.empty_like(img1)
for i in range(height-1):
    for j in range(width-1):
        for z in range(filterSize):
            if i+z-indexer < 0 or i+z-indexer > height-2:
                for tam in range(filterSize):
                    temp.append(0)
            else:
                if j+z-indexer < 0 or j+indexer > width-2:
                    temp.append(0)
                else:
                    for k in range(filterSize):
                        temp.append(img1[i+z-indexer][j+k-indexer])
        temp.sort()
        img2[i][j] = temp[len(temp)//2]
        temp = []

cv.imshow('input', img1)
cv.imshow('output', img2)

cv.waitKey(0)
cv.destroyAllWindows()
