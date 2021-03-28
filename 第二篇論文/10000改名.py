# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:27:00 2021

@author: li
"""
from PIL import Image
from os.path import join
from os import mkdir
import os
from os import listdir
from skimage import io
from os.path import join
path_input = r'D:\108RE\第二篇論文\BOWS_PNG\BOWS_PNG10000'
path_output = path_input + 'rename' 
if not os.path.isfile(path_output):
    mkdir(path_output)
files = listdir(path_input)# 取得所有檔案與子目錄名稱
i=0
for image_name in files:    
    image_path = join(path_input, image_name)
    image = Image.open(image_path)        
    image_path = join(path_output,'output{:08d}'.format(i)+".png")
    image.save(image_path)  
    i+=1