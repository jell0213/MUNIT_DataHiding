#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
import os
def mirror(name):
    image = io.imread(name+'.png')
    image_mirror = io.imread(name+'.png')
    for row in range(image.shape[0]):                                                                           
        for col in range(image.shape[1]):
            image_mirror[row][image.shape[1]-col-1][0]=image[row][col][0]
            image_mirror[row][image.shape[1]-col-1][1]=image[row][col][1]
            image_mirror[row][image.shape[1]-col-1][2]=image[row][col][2]
    io.imsave(name+'_mirror.png',image_mirror)  
mirror("oneshoe1-edge")
mirror("oneshoe2-edge")
mirror("oneshoe3-edge")
mirror("oneshoe4-edge")
mirror("oneshoe5-edge")
mirror("oneshoe6-edge")
mirror("oneshoe7-edge")
mirror("oneshoe8-edge")
mirror("oneshoe9-edge")
