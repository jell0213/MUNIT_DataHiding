#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
import random
import os
from 畫直方圖 import PH
random.seed(100)
def Embed_mod(in_dir,out_dir,edge_dir,num,mod_num):
    if not os.path.exists(out_dir) :                                                                                #建立路徑(資料夾)
        os.mkdir(out_dir)
    if not os.path.exists(out_dir+"/_Cover") :                                                                      #建立路徑_Cover，用來進行IQA比較
        os.mkdir(out_dir+"/_Cover")
    if not os.path.exists(out_dir+"/_Stego") :                                                                      #建立路徑_Stego，用來進行IQA比較
        os.mkdir(out_dir+"/_Stego")
    for i in range(num):
        if not os.path.exists(out_dir+"/output{:08d}".format(i)) :                                                  #建立路徑(各圖片子資料夾)
            os.mkdir(out_dir+"/output{:08d}".format(i))
        image = io.imread(in_dir+"/output{:08d}.png".format(i))
        io.imsave(out_dir+"/output{:08d}".format(i)+"/output{:08d}.png".format(i),image)                            #從in_dir複製原圖到out_dir
        io.imsave(out_dir+"/_Cover"+"/output{:08d}.png".format(i),image)                                            #從in_dir複製原圖到_Cover資料夾(用來進行IQA比較)
        location_map=[]
        f = open(out_dir+"/output{:08d}".format(i)+"/output{:08d}_location map.txt".format(i),'w')                  #紀錄location.txt
        image_lc = io.imread(in_dir+"/output{:08d}.png".format(i))                                                  #記錄location map(png檔)(紅：有嵌密，白：沒嵌密，黑：框(有嵌密且解密時要用到))
        image_edge = io.imread(edge_dir)                                                                            #讀取框的資料
        for row in range(image.shape[0]):                                                                           #輸入原圖，記錄location map(txt檔)，(255,255,255)為白色不可嵌密處=1，(0,0,0)為黑框可嵌密處=2，其他地方設為紅色可嵌密處=0
            location_map.append([])                                                                                 #將黑框資訊擷取出來後，可在解密時使用
            for col in range(image.shape[1]):
                location_map[row].append([])
                if image_edge[row,col] == 0 and image_edge[row, col] == 0 and image_edge[row,col] == 0:             #黑框的lc
                    location_map[row][col]= 2
                    image_lc[row,col] = [0,0,0]
                elif image[row,col,0] == 255 and image[row, col,1] == 255 and image[row,col,2] == 255:              #白色區域的lc
                    location_map[row][col]= 1
                    image_lc[row,col] = [255,255,255]
                else :                                                                                              #其他紅色區域的lc
                    location_map[row][col]= 0
                    image_lc[row,col] = [255,0,0]
                f.write(str(location_map[row][col]))
        f.close()
        io.imsave(out_dir+"/output{:08d}".format(i)+"/output{:08d}_lc.png".format(i),image_lc)
        image_embed = io.imread(in_dir+"/output{:08d}.png".format(i))                                               #嵌密
        f = open(out_dir+"/output{:08d}".format(i)+"/output{:08d}_code.txt".format(i),'w')
        for row in range(image_embed.shape[0]):
            for col in range(image_embed.shape[1]):
                if location_map[row][col]!= 1:                                                                      #紅黑可嵌密
                    image_embed[row,col,0],code=Mod(image_embed[row,col,0],mod_num)
                    f.write(str(code))
                    image_embed[row,col,1],code=Mod(image_embed[row,col,1],mod_num)
                    f.write(str(code))
                    image_embed[row,col,2],code=Mod(image_embed[row,col,2],mod_num)
                    f.write(str(code))
        f.close()
        io.imsave(out_dir+"/output{:08d}".format(i)+"/output{:08d}_embed.png".format(i),image_embed)                #儲存嵌密圖片
        io.imsave(out_dir+"/_Stego"+"/output{:08d}_embed.png".format(i),image_embed)                                #儲存嵌密圖片到_Stego資料夾(用來進行IQA比較)  
        PH(out_dir+"/output{:08d}".format(i)+"/output{:08d}.png".format(i)                                          #使用畫直方圖.py
          ,out_dir+"/output{:08d}".format(i)+"/output{:08d}_embed.png".format(i)
          ,out_dir+"/output{:08d}".format(i)+"/output{:08d}直方圖.xlsx".format(i))
def Mod(pixel,mod_num):                                                                                             #計算mod的嵌密結果
    s=random.randint(0,mod_num-1)                                                                                   #mod值沒有防呆，根據此值的範圍隨機產生數值
    p=pixel-(pixel%mod_num)                                                                                         #去掉餘數
    if p > 255-mod_num :                                                                                            #避免overflow
        p = p - mod_num
    p2=p+s                                                                                                          #加上密碼
    p3=[]                                                                                                           #生成三個數值取差異最小的，作為嵌密結果
    p3.append(p2)                                                                                                   #p,p+mod,p-mod
    if p2 > mod_num-1 :                                                                                             #避免小於0
        p3.append(p2-mod_num)
    else :
        p3.append(p2+(mod_num*2))
    if p2 < 255-mod_num+1 :                                                                                         #避免大於255
        p3.append(p2+mod_num)
    else :
        p3.append(p2-(mod_num*2))
    if abs(p3[0]-pixel)<=abs(p3[1]-pixel) and abs(p3[0]-pixel)<=abs(p3[2]-pixel) :
        return p3[0],s
    elif abs(p3[1]-pixel)<=abs(p3[0]-pixel) and abs(p3[1]-pixel)<=abs(p3[2]-pixel) :
        return p3[1],s
    else :
        return p3[2],s
Embed_mod('./oneshoe/oneshoe1-1','./oneshoe1','./oneshoe/oneshoe-edge.png',20,7)                                    #input路徑+output路徑+原框路徑+數量+mod值
Embed_mod('./oneshoe/oneshoe2-1','./oneshoe2','./oneshoe/oneshoe2-edge.png',20,7)                                   #input路徑+output路徑+原框路徑+數量+mod值
Embed_mod('./oneshoe/oneshoe3-1','./oneshoe3','./oneshoe/oneshoe3-edge.png',20,7)                                   #input路徑+output路徑+原框路徑+數量+mod值
