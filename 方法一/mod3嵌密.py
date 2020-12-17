#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
import random
import os
from 畫直方圖 import PH
random.seed(100)
def Embed_mod(test,num,directory,mod_num):
    for i in range(num):
        if not os.path.exists(test+"{:08d}".format(i)) :                            #建立路徑(資料夾)
            os.mkdir(test+"{:08d}".format(i))
        image = io.imread(directory+'\\'+test+"{:08d}.png".format(i))
        io.imsave(os.path.join(test+"{:08d}".format(i),test+'{:08d}.png'.format(i)),image)
        location_map=[]
        f = open(os.path.join(test+"{:08d}".format(i),test+'{:08d}_loaction map.txt'.format(i)),'w')                        #紀錄location.txt
        for col in range(image.shape[0]):                                           #輸入原圖，記錄location map(0:有嵌密，1:沒嵌密)，(255,255,255)為白色不可嵌密處
            location_map.append([])                                                
            for row in range(image.shape[1]):
                location_map[col].append([])
                if image[col,row,0] == 255 and image[col, row,1] == 255 and image[col,row,2] == 255: 
                    location_map[col][row]= 1
                else :
                    location_map[col][row]= 0        
                f.write(str(location_map[col][row]))
            f.write('\n')
        f.close()
        image_lc = io.imread(directory+'\\'+test+"{:08d}.png".format(i))                           #標記嵌密的地方的圖(紅：有嵌密，白，沒嵌密)
        for col in range(image_lc.shape[0]):
            for row in range(image_lc.shape[1]):
                if location_map[col][row] == 0 :
                    image_lc[col,row] = [255,0,0]
                else :
                    image_lc[col,row] = [255,255,255]
        io.imsave(os.path.join(test+"{:08d}".format(i),test+'{:08d}_lc.png'.format(i)),image_lc)
        image_embed = io.imread(directory+'\\'+test+"{:08d}.png".format(i))                        #嵌密
        f = open(os.path.join(test+"{:08d}".format(i),test+'{:08d}_code.txt'.format(i)),'w')
        for col in range(image_embed.shape[0]):
            for row in range(image_embed.shape[1]):
                if image_lc[col,row,0] == 255 and image_lc[col,row,1] == 0 and image_lc[col,row,2] == 0:    #在可嵌密處嵌密
                    image_embed[col,row,0],code=Mod(image_embed[col,row,0],mod_num)
                    f.write(str(code))
                    image_embed[col,row,1],code=Mod(image_embed[col,row,1],mod_num)
                    f.write(str(code))
                    image_embed[col,row,2],code=Mod(image_embed[col,row,2],mod_num)
                    f.write(str(code))
        f.close()
        io.imsave(os.path.join(test+"{:08d}".format(i),test+'{:08d}_embed.png'.format(i)),image_embed) 
        PH(os.path.join(test+"{:08d}".format(i),test+'{:08d}.png'.format(i))    ,    os.path.join(test+"{:08d}".format(i),test+'{:08d}_embed.png'.format(i))    ,    os.path.join(test+"{:08d}".format(i),test+'{:08d}直方圖.xlsx'.format(i))  )      
def Mod(pixel,mod_num):                                                                     #計算mod的嵌密結果
    s=random.randint(0,mod_num-1)                                                           #mod值沒有防呆，根據此值的範圍隨機產生數值
    p=pixel-(pixel%mod_num)                                                                 #去掉餘數
    if p > 255-mod_num :                                                                    #避免overflow
        p = p - mod_num
    p2=p+s                                                                                     #加上密碼
    p3=[]                                                                                    #生成三個數值取差異最小的，作為嵌密結果
    p3.append(p2)                                                                            #p,p+mod,p-mod
    if p2 > mod_num-1 :                                                                        #避免小於0
        p3.append(p2-mod_num)                                                
    else :
        p3.append(p2+(mod_num*2))
    if p2 < 255-mod_num+1 :                                                                    #避免大於255
        p3.append(p2+mod_num)
    else :
        p3.append(p2-(mod_num*2))
    if abs(p3[0]-pixel)<=abs(p3[1]-pixel) and abs(p3[0]-pixel)<=abs(p3[2]-pixel) :
        return p3[0],s
    elif abs(p3[1]-pixel)<=abs(p3[0]-pixel) and abs(p3[1]-pixel)<=abs(p3[2]-pixel) :
        return p3[1],s
    else :
        return p3[2],s
Embed_mod('output',1,'256鞋20個',5)                           #檔名+數量+資料夾名+mod值
