#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
from os import listdir
import os
import cv2
import numpy as np
from skimage import io,color,img_as_ubyte
from os.path import isfile, isdir, join, splitext
def find_peak(source1,source2):
    r=[]                                                                        #紀錄rgb
    g=[]
    b=[]
    r2=[]
    g2=[]
    b2=[]
    for i in range(256):                                                        #初始化紀錄rgb的list
        r.append(0)
        g.append(0)
        b.append(0)
        r2.append(0)
        g2.append(0)
        b2.append(0)
    image1 = io.imread(source1)                                                 #輸入圖片1(image1)
    image2 = io.imread(source2)                                                 #輸入圖片2(image2)      
    #依序將兩張圖片的RGB直方圖記錄起來
    hist = cv2.calcHist([image1], [0], None, [256], [0,256])
    hist = np.reshape(hist, (256))
    b = hist
    hist = cv2.calcHist([image1], [1], None, [256], [0,256])
    hist = np.reshape(hist, (256))
    g = hist
    hist = cv2.calcHist([image1], [2], None, [256], [0,256])
    hist = np.reshape(hist, (256))
    r = hist
    hist2 = cv2.calcHist([image2], [0], None, [256], [0,256])
    hist2 = np.reshape(hist2, (256))
    b2 = hist2
    hist2 = cv2.calcHist([image2], [1], None, [256], [0,256])
    hist2 = np.reshape(hist2, (256))
    g2 = hist2
    hist2 = cv2.calcHist([image2], [2], None, [256], [0,256])
    hist2 = np.reshape(hist2, (256))
    r2 = hist2
    peak=[]
    count1=0#算PEAK數
    count2=0
    dc=0
    ds=0
    #算DC、DS
    for i in range(253):
        if (r[i+1] > r[i] and r[i+1] > r[i+2]) or (r[i+1] < r[i] and r[i+1] < r[i+2]) :
            #count1+=1
            dc+=abs(2*r[i+1]-r[i]-r[i+2])
    for i in range(253):
        if (r2[i+1] > r2[i] and r2[i+1] > r2[i+2]) or (r2[i+1] < r2[i] and r2[i+1] < r2[i+2]) :
            #count2+=1
            ds+=abs(2*r2[i+1]-r2[i]-r2[i+2])
    return dc,ds
mypath = "C:\\Users\\Ian\\Desktop\\100%\\_Cover(100%)"
mypath2 = "C:\\Users\\Ian\\Desktop\\100%\\_Stego(100%)"
files = listdir(mypath)# 取得所有檔案與子目錄名稱
files2 = listdir(mypath2)# 取得所有檔案與子目錄名稱
dcb=0
dsb=0
i=0
for f in files :
    f2=files2[i]
    i+=1
    fullpath = join(mypath, f)
    image = io.imread(fullpath)
    fullpath2 = join(mypath2, f2)
    image2 = io.imread(fullpath2)
    a,b=find_peak(fullpath,fullpath2)
    if a > b:
        dcb+=1
    if b > a:        
        dsb+=1
    if i%250==0 :
        print(i)
print(dcb)
print(dsb)
