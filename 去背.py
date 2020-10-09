#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image

image = Image.open('input.png')
#for item in image.getdata():
    #print(item)    
image = image.convert('RGBA')
print(image.mode)


# Transparency
newImage = []
for item in image.getdata():
    #print(item)
    if item[:3] == (255, 255, 255):
        newImage.append((255, 255, 255, 0))
    else:
        newImage.append(item)

image.putdata(newImage)
image = image.convert('RGB')
for item in image.getdata():
    print(item) 

image.save('output.png')
print(image.mode, image.size)

image = Image.open('output.png')
print(image)
image.save('output.png')
