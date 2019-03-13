import cv2 as cv 
import numpy as np 

img = cv.imread('pic1.jpg',cv.IMREAD_GRAYSCALE)
height , width = img.shape
img1D= img.cumsum()
uniques , counts = np.unique(img,return_counts=True)
Dic1 = dict(zip(uniques,counts))
count_hist = []
for i in range(len(Dic1)):
    count_hist.append(Dic1[i])

# for i in range(len(count_hist)):
#     print(count_hist[i])
for i in range(len(count_hist)):
    if i == 0:
        count_hist[0]=count_hist[0]
    else:
        count_hist[i]=count_hist[i-1]+count_hist[i]

count1 = np.array(count_hist)
for i in range(len(count1)):
    count1[i] = count1[i]*255//count1.max()
# for i in range(len(count1)):
#     print(count1[i])

img2 = np.empty_like(img)
for i in range(height):
    for j in range(width):
        img2[i][j] = count1[img[i][j]]

cv.imshow('input',img)
cv.imshow('output',img2)

cv.waitKey(0)
cv.destroyAllWindows()





