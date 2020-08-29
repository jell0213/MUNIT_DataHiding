#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
def pic_compare(name1,name2):
    image = io.imread(name1)
    image2 = io.imread(name2)
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
for i in range(20):
    pic_compare("./oneshoe/oneshoe1-1/output{:08d}.png".format(i),"./oneshoe/oneshoe1-2/output{:08d}.png".format(i))
for i in range(20):
    pic_compare("./oneshoe/oneshoe2-1/output{:08d}.png".format(i),"./oneshoe/oneshoe2-2/output{:08d}.png".format(i))
for i in range(20):
    pic_compare("./oneshoe/oneshoe3-1/output{:08d}.png".format(i),"./oneshoe/oneshoe3-2/output{:08d}.png".format(i))
