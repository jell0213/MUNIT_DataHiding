# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from skimage import io
from os.path import join
from openpyxl import Workbook
#############################分別印出路徑中所有圖片的像素值(excel檔)
def Print_pixel():
    mypath=str(input("請輸入路徑"))#資料夾路徑
    files = listdir(mypath)# 取得所有檔案與子目錄名稱
    #對每張圖片進行處理，分別產生一個excel檔    
    for f in files:
        path_image = join(mypath, f)
        image = io.imread(path_image)
        f=f[:-4]#去掉".png"以便命名
        path_excel = join(mypath,f+"_display.xlsx")
        wb = Workbook()
        ws = wb.active
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                ws.cell(row=row+1, column=col+1,value=
                        str(image[row,col,0])+"/"+
                        str(image[row,col,1])+"/"+
                        str(image[row,col,2]))
        wb.save(path_excel)
        print(f+"-complete")
Print_pixel()