import numpy as np 
import cv2 as cv 

def medianFilter(input,filterSize):
    height = len(input)
    width = len(input[0])
    output = np.empty_like(input)
    indexer = filterSize//2
    temp = []
    for i in range(height):
        for j in range(width):
            for k in range(filterSize):
                if i+k-indexer <0 or i+k+indexer>height-1:
                    for tam1 in range(filterSize):
                        temp.append(0)
                elif j+k - indexer < 0 or j+k+indexer>width-1:
                    for tam2 in range(filterSize):
                        temp.append(0)
                else:g




for i in range(10):
    print(i)