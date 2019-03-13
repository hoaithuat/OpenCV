import cv2 as cv 
import numpy as np 
from scipy import ndimage

img = cv.imread('pic1.png',cv.IMREAD_GRAYSCALE)
ddept = -1
kerrne_size = 3
filter_laplacian1 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)
filter_laplacian2 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],np.float32)
filter_sobel1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]],np.float32)
filter_sobel2 = np.array([[-1,0, 1],[-2,0,2],[-1,0,1]],np.float32)

img1 = cv.filter2D(img,ddept,filter_laplacian1)
# height , width = img1.shape
# for i in range(height):
#     for j in range(width):
#         img1[i][j]  = 255-img1[i][j]

img2 = ndimage.convolve(img,filter_laplacian2)
img3= img+img1
# unshape_masking = img - img2
cv.imshow('input',img)
cv.imshow('output1',img1)
cv.imshow('output2',img2)
# cv.imshow('output3',img3)
# cv.imshow('unshape',unshape_masking)


cv.waitKey(0)
cv.destroyAllWindows()  