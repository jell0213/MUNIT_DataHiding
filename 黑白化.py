#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
def blackandwhite(name):
    image = io.imread(name+".png")
    for col in range(image.shape[0]):
        for row in range(image.shape[1]):
            if image[col,row,0] > 30 or image[col,row,1] > 30 or image[col,row,2] > 30 :
                image[col,row] = [255,255,255]
            else :
                image[col,row] = [0,0,0]
    io.imsave(name+"-b&w.png",image) 
blackandwhite("bag_edge")
