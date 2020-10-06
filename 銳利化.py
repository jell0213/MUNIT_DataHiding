#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import cv2 as cv
import numpy as np
def sharpen(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #銳化
    dst = cv.filter2D(image, -1, kernel=kernel)   
    cv.imwrite("output00000000_sharpen.png",dst)
for i in range(1):
    for j in range(1):
        src = cv.imread("./m/png/m9/output00000000.png")
        sharpen(src)


