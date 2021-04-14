<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
處理檔名只有數字的png影像
輸入：一個資料夾路徑
處理：所有輸入路徑的影像
輸出：另一資料夾路徑
"""
from PIL import Image
from os.path import join
from os import mkdir
import os
from os import listdir
from skimage import io
from os.path import join

def rename(path_input):
    path_output = path_input + 'rename' 
    if not os.path.exists(path_output):
        mkdir(path_output)
    files = listdir(path_input)# 取得所有檔案與子目錄名稱
    i=0
    for image_name in files:    
        image_path = join(path_input, image_name)
        image = Image.open(image_path)         
        image_name=image_name.replace('.png', '')#刪除檔案類型字串
        image_name=int(image_name)#把檔名數字str轉int
        image_name="{:08d}".format(image_name)+".png"#把.png補回
        image_path = join(path_output,image_name)
        image.save(image_path)  
path_input = r'D:\108RE\第二篇論文\BOWS_PNG2\BOWS_PNG10000'
rename(path_input)
=======
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
>>>>>>> 626064154e3f93f41a487db1b25eef2ea9e15c63
