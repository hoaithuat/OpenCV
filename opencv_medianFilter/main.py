#Program Median Filter
#Kernel 3x3

import cv2 as cv
import numpy as np

img1 = cv.imread('pic1.png',cv.IMREAD_GRAYSCALE)
img2 = np.empty_like(img1)
height = len(img1)
width = len(img1[0])

for i in range(height-1):
    for j in range(width-1):
        if j == 0:
            if i ==0:
                members = [(0,0)]*4
                members[0] = img1[0][0]
                members[1] = img1[0][1]
                members[2] = img1[1][0]
                members[3] = img1[1][1]
                members.sort()
                img2[i][j]=members[2]
            elif i== height:
                members = [(0, 0)] * 4
                members[0] = img1[height-1][0]
                members[1] = img1[height - 1][1]
                members[2] = img1[height][0]
                members[3] = img1[height][1]
                members.sort()
                img2[i][j] = members[2]
            else:
                members = [(0, 0)] * 6
                members[0] = img1[i-1][0]
                members[1] = img1[i-1][1]
                members[2] = img1[i][0]
                members[3] = img1[i][1]
                members[4] = img1[i+1][0]
                members[5] = img1[i+1][1]
                members.sort()
                img2[i][j] = members[3]
        elif j == width:
            if i ==0:
                members = [(0, 0)] * 4
                members[0] = img1[width-1][0]
                members[1] = img1[width][0]
                members[2] = img1[width-1][1]
                members[3] = img1[width][1]
                members.sort()
                img2[i][j] = members[2]
            elif i == height:
                members = [(0, 0)] * 4
                members[0] = img1[height-1][width-1]
                members[1] = img1[height-1][width]
                members[2] = img1[height][width-1]
                members[3] = img1[height][width]
                members.sort()
                img2[i][j] = members[2]
            else:
                members = [(0,0)]*6
                members[0] = img1[i-1][j-1]
                members[1] = img1[i-1][j]
                members[2] = img1[i][j-1]
                members[3] = img1[i][j]
                members[4] = img1[i+1][j-1]
                members[5] = img1[i+1][j]
                members.sort()
                img2[i][j] = members[3]
        else:
            if i == 0 :
                members = [(0,0)]*6
                members[0] = img1[i][j-1]
                members[1] = img1[i][j]
                members[2] = img1[i][j+1]
                members[3] = img1[i+1][j-1]
                members[4] = img1[i+1][j]
                members[5] = img1[i+1][j+1]
                members.sort()
                img2[i][j] = members[3]
            elif i == height:
                members =[(0,0)]*6
                members[0] = img1[i-1][j-1]
                members[1] = img1[i-1][j]
                members[2] = img1[i-1][j+1]
                members[3] = img1[i][j-1]
                members[4] = img1[i][j]
                members[5] = img1[i][j+1]
                members.sort()
                img2[i][j] = members[3]

            else:
                members = [(0, 0)]*9
                members[0] = img1[i-1][j-1]
                members[1] = img1[i-1][j]
                members[2] = img1[i-1][j+1]
                members[3] = img1[i][j-1]
                members[4] = img1[i][j]
                members[5] = img1[i][j+1]
                members[6] = img1[i+1][j-1]
                members[7] = img1[i+1][j]
                members[8] = img1[i+1][j+1]
                members.sort()
                img2[i][j] = members[4]


cv.imshow('input',img1)
cv.imshow('output',img2)
cv.waitKey(0)
cv.destroyAllWindows()
