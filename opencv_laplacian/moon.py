import cv2 as cv 
import numpy as np 
from scipy import ndimage

#ImgA is original picture
imgA = cv.imread('moon.tif',cv.IMREAD_GRAYSCALE)
ddept = -1
kerrne_size = 3
filter_laplacian1 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
filter_laplacian2 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]],np.float32)
filter_laplacian3 = np.array([[0,0,0],[0,1,0],[0,0,0]],np.float32)

filter_sobel1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]],np.float32)
filter_sobel2 = np.array([[-1,0, 1],[-2,0,2],[-1,0,1]],np.float32)

#ImgB is picture output of imgA and laplacian filter
imgB = cv.filter2D(imgA,ddept,filter_laplacian2)
imgB1 = cv.filter2D(imgA,ddept,filter_laplacian3)
# imgC = imgB+imgB1

height , width = imgB.shape

# imgB1 = np.empty_like(imgB)
# for i in range(height):
#     for j in range(width):
#         imgB1[i][j] = 255 - imgB[i][j]

# dem =0
# for i in range(height):
#     for j in range(width):
#         if (imgB[i][j]<0):
#             dem = dem+1
# print(dem)

imgOut = imgA+imgB

cv.imshow('input',imgA)
cv.imshow('imgB',imgB)
# cv.imshow('Output',imgC)



cv.waitKey(0)
cv.destroyAllWindows()  