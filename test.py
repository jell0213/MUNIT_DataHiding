#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
from os import listdir
import os
from skimage import io,color,img_as_ubyte
from os.path import isfile, isdir, join, splitext
mypath = "../9.22-meeting/鏡像/png/鏡像1/border/"
if not os.path.exists(mypath+"/test") :                                                                                #建立路徑(資料夾)
        os.mkdir(mypath+"/test")
files = listdir(mypath)# 取得所有檔案與子目錄名稱
for f in files :
    fullpath = join(mypath, f)
    image = io.imread(fullpath)
    path2 = mypath+"/test/"+f
    io.imsave(path2,image)
    print(str(fullpath))
'''
for i in range(10):
    print(i)
'''
# 找出指定目錄下的所有.csv檔
from os import listdir
from os.path import isfile, isdir, join, splitext

# 目錄位置-要找出目錄下的所有檔案清單
mypath = "C:\\Users\\sya\\Downloads"

# 取得所有檔案與子目錄名稱
files = listdir(mypath)

# 要移除的清單 (不是.csv的檔案)
removelist = list() 
 
# 迴圈讀取目錄下的檔案
for f in files:
 
# 組合出檔案的絕對路徑
fullpath = join(mypath, f)
 
# 只處理 fullpath 是檔案的項目(略過目錄)
if isfile(fullpath):
    if splitext(f)[1] != '.csv':
    removelist.append(f)

# 從files中移除不是.csv的檔案
for item in removelist:
    files.remove(item)
'''
