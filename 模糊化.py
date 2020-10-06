#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import cv2 as cv
import numpy as np
def blur_demo(image):
    dst = cv.blur(image, (15, 1))                                   #模糊化
    cv.imwrite("output00000000_blur.png",dst)
src = cv.imread("output00000000.png")
blur_demo(src)
