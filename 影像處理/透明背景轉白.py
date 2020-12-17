#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
for i in range(10):
    image = Image.open('output{:08d}.png'.format(i))
    newImage = []
    for item in image.getdata():
        if item[:4] == (0, 0, 0 , 0):                   #將透明區(0,0,0,0)轉成(255,255,255)
            newImage.append((255, 255, 255))
        else:
            newImage.append(item)
    image.putdata(newImage)
    image = image.convert('RGB')#RGBA轉RGB
    image.save('output{:08d}_removebg.png'.format(i))
