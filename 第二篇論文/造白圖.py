# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:53:15 2021

@author: li


"""
from skimage import io
#import numpy as np
import cv2
image = io.imread(r'C:\Users\li\Desktop\test\1.png')

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i][j]=(255,255,255)
for i in range(10000):
    cv2.imwrite(r'C:\Users\li\Desktop\white2\white2-10000\{:d}.png'.format(i+1),image)
    
    
    
    #size = (512, 512)
    # 全黑.可以用在屏保
    #black = np.zeros(size)
    #print(black[34][56])
    #cv2.imwrite(r'C:\Users\li\Desktop\white\testblack.png',black)
    #white 全白
    
    #black[:]=255
    #print(black[34][56])
    #cv2.imwrite(r'C:\Users\li\Desktop\white\white10000\{:08d}.png'.format(i+1),black)
    