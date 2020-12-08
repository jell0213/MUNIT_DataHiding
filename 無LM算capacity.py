# -*- coding: utf-8 -*-
#######################################################
'''
input
    路徑
    圖片數量
    MOD值
    嵌密率
處理內容
    輸入一張圖片的資料，包含：
        1.資料夾名稱
        2.檔案名稱(圖片)，單純用來記錄在xlsx檔案中
        3.輸出路徑-xlsx
        4.嵌密mod值
        5.嵌密率
output
    產生輸入圖片的xlsx檔(依序將所有圖片的資料寫入xlsx檔中)      
        包含執行時間
'''
#######################################################
from skimage import io
from openpyxl import Workbook
import openpyxl
import os
import math
import time
def cal_capacity(in_dir,
                 num_image,
                 num_mod,
                 embed_ratio):
    wb = Workbook()
    ws = wb.active
    ws.append(["無LM","mod="+str(num_mod),str(embed_ratio)+"%","256*256"])
    ws.append(["檔名","嵌密量","bpp"])
    a=[]                                                                                                    #儲存各項平均值
    for i in range(2):
        a.append(0)
    for i in range(num_image):
        f_code= open(in_dir+"/output{:08d}".format(i)+"/output{:08d}_code.txt".format(i),'r')               #打開location map.txt來計算capacity
        words = f_code.read()
        num_words = len(words) 
        num_words*=math.log(num_mod,2)                                                    #capacity
        bpp=num_words/(256*256)                                                              #嵌入率(%)(txt和png相同)        
        ws.append(["output{:08d}".format(i),
                   float('%.2f'%round(num_words,2)),                                                        #四捨五入到指定小數位
                   float('%.2f'%round(bpp,2))])
        a[0]+=num_words
        a[1]+=bpp
        if i % 250 == 0 :
            print(i)
    for i in range(2):
        a[i]/=num_image
    ws.append(["檔名","嵌密量","bpp"])
    ws.append([
            "",
            float('%.2f'%round(a[0],2)),            
            float('%.2f'%round(a[1],2)),
            ])
    wb.save(in_dir+"/NLM-mod{:d}_capacity".format(num_mod)+"({:d}%).xlsx".format(embed_ratio))              #寫檔後存檔
#---------------------------------------------------------------------------設定區
in_dir="D:\\108resercher\\====######RESEARCH######====\\GAN-research\\12.8\\無LM嵌密結果\\100%MOD3"           
num_image = 5000
num_mod = 3
embed_ratio= 100
#---------------------------------------------------------------------------設定區
tStart = time.time()                                                                                        #計時開始
cal_capacity(in_dir,num_image,num_mod,embed_ratio)                                                          #執行程式
tEnd = time.time()                                                                                          #計時結束
wb = openpyxl.load_workbook(in_dir+"/NLM-mod{:d}_capacity".format(num_mod)+"({:d}%).xlsx".format(embed_ratio))
ws = wb['Sheet']
ws.append(["total time",str(round(tEnd-tStart,2))+" s"])
wb.save(in_dir+"/NLM-mod{:d}_capacity".format(num_mod)+"({:d}%).xlsx".format(embed_ratio))                  #寫檔後存檔
