#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#5000張256*256---->15秒
from PIL import Image
from os.path import join
from os import mkdir
import os
'''
def resize_small(path_input,path_output,image_number,image_type):
    
    path_image = join(path_input,image_number+image_type) 
    img = Image.open(path_image)
    new_img = img.resize((64, 64))
    path_image2 = join(path_output,image_number+"_small.png")
    new_img.save(path_image2)

path_input = 'C:/Users/li/Desktop/test'
path_output = 'C:/Users/li/Desktop/test/test2'
mkdir(path_output)
for i in range(3): 
    image_number="output{:08d}".format(i)
    image_type="_embed.png"
    resize_small(path_input,path_output,image_number,image_type)
'''
from os import listdir
from skimage import io
from os.path import join
def batch_resize(path_input,path_output,size):
    files = listdir(path_input)# 取得所有檔案與子目錄名稱
    for image_name in files:  
        image_path = join(path_input, image_name)
        image = Image.open(image_path)    
        resize_image = image.resize((size, size))
        resize_image_name = image_name.split('.')[0]+'_'+str(size)
        resize_image_path = join(path_output,resize_image_name+".png")
        resize_image.save(resize_image_path)        
path_input = r'D:\108RE\第二篇論文\BOWS_PNG\BOWS_PNG10000'
#size = int(input("input size : "))
size = 256
path_output = path_input + str(size) + '-' + str(size) 
if not os.path.isfile(path_output):
    mkdir(path_output)
batch_resize(path_input,path_output,size)
size = 128
path_output = path_input + str(size) + '-' + str(size) 
if not os.path.isfile(path_output):
    mkdir(path_output)
batch_resize(path_input,path_output,size)
size = 64
path_output = path_input + str(size) + '-' + str(size) 
if not os.path.isfile(path_output):
    mkdir(path_output)
batch_resize(path_input,path_output,size)
size = 32
path_output = path_input + str(size) + '-' + str(size) 
if not os.path.isfile(path_output):
    mkdir(path_output)
batch_resize(path_input,path_output,size)
size = 16
path_output = path_input + str(size) + '-' + str(size) 
if not os.path.isfile(path_output):
    mkdir(path_output)
batch_resize(path_input,path_output,size)
size = 8
path_output = path_input + str(size) + '-' + str(size) 
if not os.path.isfile(path_output):
    mkdir(path_output)
batch_resize(path_input,path_output,size)
