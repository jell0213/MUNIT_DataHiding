#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
def Check_Mod3(source1,source2):
    image = io.imread(source1)
    image2 = io.imread(source2)
    for i in range(image.shape[1]):
        print(str(image[127,i])+'---'+str(image2[127,i]))
test='output00000000'
Check_Mod3(test+"\\"+test+".png",test+"\\"+test+"_embed.png")
