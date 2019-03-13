import cv2 as cv 
import numpy as np 
from scipy import ndimage

#ImgA is original picture
imgA = cv.imread('bone.tif',cv.IMREAD_GRAYSCALE)
ddept = -1
kerrne_size = 3
filter_laplacian1 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
filter_laplacian2 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]],np.float32)
filter_sobel1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]],np.float32)
filter_sobel2 = np.array([[-1,0, 1],[-2,0,2],[-1,0,1]],np.float32)

#ImgB is picture output of imgA and laplacian filter
imgB = cv.filter2D(imgA,ddept,filter_laplacian2)
imgB1 = ndimage.convolve(imgA,filter_laplacian1)
imgB1 = np.array(imgB1)

imgC = imgA + imgB
# imgSob1 = cv.filter2D(img,ddept,filter_sobel1)
# imgSob2 = cv.filter2D(img,ddept,filter_sobel2)
# img3 = imgSob1 + imgSob2
sobelx = cv.Sobel(imgA,-1,1,0,ksize=5)
sobely = cv.Sobel(imgA,-1,0,1,ksize=5)
ImgD = sobelx+sobely
# img2        -= np.amin(img2)
# img2        *= 255.0/np.amax(img2)

imgE = cv.blur(ImgD,(5,5))
# imgF =(imgC - imgE)//2
# unshape_masking = img - img2
# cv.imshow('input',img)
cv.imshow('imgF',imgC)
cv.imshow('Sobel',ImgD)
cv.imshow('Sobel blur 5x5 ',imgE)
# cv.imshow('unshape',unshape_masking)


cv.waitKey(0)
cv.destroyAllWindows()  