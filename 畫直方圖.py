# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
from openpyxl import Workbook,chart
def PH(source1,source2,result):                                                         #定義一個HE的函數
    r=[]                                                                        #紀錄rgb
    g=[]
    b=[]
    r2=[]
    g2=[]
    b2=[]
    wb = Workbook()
    ws = wb.active
    for i in range(256):                                                        #初始化紀錄rgb的list
        r.append(0)
        g.append(0)
        b.append(0)
        r2.append(0)
        g2.append(0)
        b2.append(0)
    image1 = io.imread(source1)                                                 #輸入圖片(image1)
    image2 = io.imread(source2)                                                 #輸入圖片(imager)      
    for col in range(image1.shape[0]):                                          #紀錄轉換前的rgb
        for row in range(image1.shape[1]):  
            r[image1[col,row,0]]+=1
            g[image1[col,row,1]]+=1
            b[image1[col,row,2]]+=1
    for col in range(image2.shape[0]):                                          #紀錄轉換後的rgb
        for row in range(image2.shape[1]):  
            r2[image2[col,row,0]]+=1
            g2[image2[col,row,1]]+=1
            b2[image2[col,row,2]]+=1
    print(result,"-----> finish")
    ws.append([result])
    ws.append([str(image1.shape[0])+"*"+str(image1.shape[1])])    
    ws.append(["","","before","","","after"])
    ws.append(["resolution","value","Red","Green","Blue","Red","Green","Blue"])
    for i in range(256):
        ws.append([str(image1.shape[0]*image1.shape[1]),i,r[i],g[i],b[i],r2[i],g2[i],b2[i]])
    a = chart.Reference(ws, min_row=5, min_col=3, max_row=260, max_col=3)       #劃出直方圖-R1
    s1 = chart.Series(a, title='')
    c1 = chart.BarChart()
    c1.title = 'R1'
    c1.style = 4
    c1.append(s1)
    ws.add_chart(c1,'J5')  
    a = chart.Reference(ws, min_row=5, min_col=4, max_row=260, max_col=4)       #劃出直方圖-G1
    s2 = chart.Series(a, title='')
    c2 = chart.BarChart()
    c2.title = 'G1'
    c2.style = 5
    c2.append(s2)
    ws.add_chart(c2,'J20')  
    a = chart.Reference(ws, min_row=5, min_col=5, max_row=260, max_col=5)       #劃出直方圖-B1
    s3 = chart.Series(a, title='')
    c3 = chart.BarChart()
    c3.title = 'B1'
    c3.append(s3)
    ws.add_chart(c3,'J35')         
    a = chart.Reference(ws, min_row=5, min_col=6, max_row=260, max_col=6)       #劃出直方圖-R2
    s4 = chart.Series(a, title='')
    c4 = chart.BarChart()
    c4.title = 'R2'
    c4.style = 4
    c4.append(s4)
    ws.add_chart(c4,'S5')  
    a = chart.Reference(ws, min_row=5, min_col=7, max_row=260, max_col=7)       #劃出直方圖-G2
    s5 = chart.Series(a, title='')
    c5 = chart.BarChart()
    c5.title = 'G2'
    c5.style = 5
    c5.append(s5)
    ws.add_chart(c5,'S20')  
    a = chart.Reference(ws, min_row=5, min_col=8, max_row=260, max_col=8)       #劃出直方圖-B2
    s6 = chart.Series(a, title='')
    c6 = chart.BarChart()
    c6.title = 'B2'
    c6.append(s6)
    ws.add_chart(c6,'S35')  
    wb.save(result)   
    #print(r[1])
    #print(r2[1])
#test='shoe2'
#PH(test+'_color.png',test+'_embed.png',test+'直方圖.xlsx')
