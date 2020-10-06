#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
import os
def border(edge,source,j):
    image_edge = io.imread(edge+".png")
    image = io.imread(source+".png")
    for row in range(image.shape[0]):                                                                          #將黑框資訊擷取出來後，可在解密時使用
        for col in range(image.shape[1]):
            #if image_edge[row,col,0] == 0 and image_edge[row, col,1] == 0 and image_edge[row,col,2] == 0:             #黑框的lc
            if image_edge[row,col] == 0:
                image[row,col] = [0,0,0]
    io.imsave(source+"_border.png",image)
for j in range(200):
    border("bag1-edge","output{:08d}".format(j),j)
