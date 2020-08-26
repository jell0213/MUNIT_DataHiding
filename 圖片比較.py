#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
image = io.imread("一隻鞋.png")
image2 = io.imread("bag_edge.png")
count=0
for col in range(image.shape[0]):
    for row in range(image.shape[1]):
        count+=image[col,row,0]
        count-=image2[col,row,0]
        count+=image[col,row,1]
        count-=image2[col,row,1]
        count+=image[col,row,2]
        count-=image2[col,row,2]
if count == 0 :
    print("same")
else :
    print("different")
print (count)
