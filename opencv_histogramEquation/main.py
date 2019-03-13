import cv2 as cv 
import numpy as np

img = cv.imread('pic1.jpg',cv.IMREAD_GRAYSCALE)
img1D = []
heightImg , widthImg = img.shape
img1D = np.cumsum(img)
img1D = list(img1D)
img1D.sort()

count = []
for i in range(255):
    dem = img1D.count(i)
    count.append(dem)


count_hist = np.empty_like(count)
for i in range(len(count)):
    if i ==0:
        count_hist[i]=count[i]
    else:
        count_hist [i] = count_hist[i-1]+count[i]
for i in range(len(count_hist)):
    count_hist[i]=count_hist[i]*255//count_hist.max()


# for i in range(heightImg):
#     for j in range(widthImg):
#         A = img[i][j]
#         img[i][j] = count_hist[A]
img2 = count_hist[img]

cv.imshow('Output',img2)

print(len(img1D))
print(heightImg)
print(widthImg)