#!/usr/bin/env python
# -*- coding: utf-8 -*-
####################################################
'''
input:
    一個資料夾中output格式的圖片
        1.input路徑
        2.output路徑
        3.mod值
        4.影像數量
output:
    cover資料夾(原圖)
    stego資料夾(嵌密影像)
    每個圖片都有一個資料夾:
        1.原圖
        2.密碼
        3.嵌密影像
        4.location map(png)
        5.location map(txt)
        6.直方圖
'''
####################################################
from skimage import io,color,img_as_ubyte
import random
import os
from 畫直方圖 import PH
random.seed(100)
def Embed_mod(in_dir,out_dir,mod_num,num):
    print("embed ratio = 100%")                                                                                     #嵌密率100%
    if not os.path.exists(out_dir):                                                                                 #建立路徑(資料夾)
        os.mkdir(out_dir)
    if not os.path.exists(out_dir+"/_Cover") :                                                                      #-----------建立路徑_Cover，用來進行IQA比較
        os.mkdir(out_dir+"/_Cover")
    if not os.path.exists(out_dir+"/_Stego") :                                                                      #-----------建立路徑_Stego，用來進行IQA比較
        os.mkdir(out_dir+"/_Stego")
    for i in range(num):
        if not os.path.exists(out_dir+"/output{:08d}".format(i)) :                                                  #-----------建立路徑(各圖片子資料夾)
            os.mkdir(out_dir+"/output{:08d}".format(i))
        image = io.imread(in_dir+"/output{:08d}.png".format(i))
        io.imsave(out_dir+"/output{:08d}".format(i)+"/output{:08d}.png".format(i),image)                            #-----------從in_dir複製原圖到out_dir
        io.imsave(out_dir+"/_Cover"+"/output{:08d}.png".format(i),image)                                            #-----------從in_dir複製原圖到_Cover資料夾(用來進行IQA比較)
        location_map=[]
        f = open(out_dir+"/output{:08d}".format(i)+"/output{:08d}_lc.txt".format(i),'w')                            #-----------紀錄lc.txt
        image_lc = io.imread(in_dir+"/output{:08d}.png".format(i))                                                  #-----------記錄lc.png(png檔)(紅：有嵌密，白：沒嵌密)
        for row in range(image.shape[0]):                                                                           #輸入原圖，記錄lc.txt，(255,255,255)為白色不可嵌密處=1，其他地方設為紅色可嵌密處=0
            location_map.append([])                                                                                 
            for col in range(image.shape[1]):
                location_map[row].append([])
                if image[row,col,0] == 255 and image[row, col,1] == 255 and image[row,col,2] == 255:                #白色區域的lc
                    location_map[row][col]= 1
                    image_lc[row,col] = [255,255,255]
                else :                                                                                              #其他紅色區域的lc
                    location_map[row][col]= 0
                    image_lc[row,col] = [255,0,0]
                f.write(str(location_map[row][col]))
        f.close()
        io.imsave(out_dir+"/output{:08d}".format(i)+"/output{:08d}_lc.png".format(i),image_lc)
        image_embed = io.imread(in_dir+"/output{:08d}.png".format(i))                                               #嵌密
        f = open(out_dir+"/output{:08d}".format(i)+"/output{:08d}_code.txt".format(i),'w')                          #紀錄秘密訊息
        pixel_num = 0                                                                                               #pixel_num用來處理嵌密率(僅在可嵌區域中遞增)
        embed_count = 0
        for row in range(image_embed.shape[0]):
            for col in range(image_embed.shape[1]):                
                if location_map[row][col]!= 1 :                                                                     #紅黑可嵌密
                    if (pixel_num%2) < 2 :                                                                          #pixel_num對100取餘數，如果小於嵌密率，就進行嵌密
                        image_embed[row,col,0],code=Mod(image_embed[row,col,0],mod_num)                             #回傳兩值(嵌密,祕密訊息)
                        f.write(str(code))
                        image_embed[row,col,1],code=Mod(image_embed[row,col,1],mod_num)
                        f.write(str(code))
                        image_embed[row,col,2],code=Mod(image_embed[row,col,2],mod_num)
                        f.write(str(code))
                        embed_count += 1                                                                            #embed_count紀錄實際有嵌密的pixel數量(僅檢驗用)
                    pixel_num += 1
        print(embed_count)
        f.close()
########################################################################################################################################################################檢查非白
        location_map2=[]
        f = open(out_dir+"/output{:08d}".format(i)+"/output{:08d}_lc2.txt".format(i),'w')                           #-----------紀錄lc2.txt
        image_lc2 = io.imread(in_dir+"/output{:08d}.png".format(i))                                                 #-----------記錄lc2.png(png檔)(紅：有嵌密，白：沒嵌密)
        for row in range(image.shape[0]):                                                                           #輸入原圖，記錄lc2.txt，(255,255,255)為白色不可嵌密處=1，其他地方設為紅色可嵌密處=0
            location_map2.append([])                                                                                 
            for col in range(image.shape[1]):
                location_map2[row].append([])
        for row in range(image_embed.shape[0]):
            for col in range(image_embed.shape[1]):                
                if location_map[row][col]!= 1 :                                                                     #紅黑可嵌密
                    if (pixel_num%2) < 2 :                                                                          #pixel_num對100取餘數，如果小於嵌密率，就進行嵌密
                        image_embed[row,col,0],code=Mod(image_embed[row,col,0],mod_num)                             #回傳兩值(嵌密,祕密訊息)
                        f.write(str(code))
                        image_embed[row,col,1],code=Mod(image_embed[row,col,1],mod_num)
                        f.write(str(code))
                        image_embed[row,col,2],code=Mod(image_embed[row,col,2],mod_num)
                        f.write(str(code))
                        embed_count += 1                                                                            #embed_count紀錄實際有嵌密的pixel數量(僅檢驗用)
                    pixel_num += 1
                    
                    
        io.imsave(out_dir+"/output{:08d}".format(i)+"/output{:08d}_embed.png".format(i),image_embed)                #------------儲存嵌密圖片
        io.imsave(out_dir+"/_Stego"+"/output{:08d}_embed.png".format(i),image_embed)                                #------------儲存嵌密圖片到_Stego資料夾(用來進行IQA比較)  
        PH(out_dir+"/output{:08d}".format(i)+"/output{:08d}.png".format(i)                                          #使用畫直方圖.py
          ,out_dir+"/output{:08d}".format(i)+"/output{:08d}_embed.png".format(i)
          ,out_dir+"/output{:08d}".format(i)+"/output{:08d}直方圖.xlsx".format(i))
def Mod(pixel,mod_num):                                                                                             #計算mod的嵌密結果
    s=random.randint(0,mod_num-1)                                                                                   #mod值沒有防呆，根據此值的範圍隨機產生數值
    r=pixel%mod_num
    d=[(s-r)+mod_num]%mod_num
    if d == 0:
        pp=pixel
    elif d < (mod_num/2) :
        pp=pixel+d
    else :
        pp=pixel+d-mod_num
    if pp<0 :
        pp=pp+mod_num
    elif pp > 255 :
        pp=pp-mod_num
    else:
        pp=pp
    return pp,s

#Embed_mod('./100%','./100%/embed_mod3','./100%/input.png',5000)
Embed_mod('./100%','./100%/embed_mod3',3,1)
