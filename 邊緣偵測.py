#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
def getedge(name):
    while(1):
        image = cv2.imread(name+".png")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                      #轉灰階
        b=int(input("blur = "))
        if b == 0 :
            break
        t1=int(input("threshold 1 = "))
        t2=int(input("threshold 2 = "))
        blurred = cv2.GaussianBlur(gray, (b, b), 0)                         #高斯模糊
        canny = cv2.Canny(blurred, t1, t2)                                  #邊緣偵測
        ret,thresh = cv2.threshold(canny,127,255,cv2.THRESH_BINARY_INV)     #反白
        #cv2.imwrite('['+str(b)+']'+str(t1)+'-'+str(t2)+'.jpg', thresh)     #寫檔
        cv2.imwrite(name+'-edge.png', thresh)
getedge("oneshoe1")

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
name = input("picture name:")   #輸入檔名
image = cv2.imread(name)    #讀檔
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #轉灰階
blurred = cv2.GaussianBlur(gray, (5, 5), 0)     #高斯模糊
canny = cv2.Canny(blurred, 30, 150) #邊緣偵測
ret,thresh = cv2.threshold(canny,127,255,cv2.THRESH_BINARY_INV)     #反白
cv2.imshow('Input', image)
cv2.imshow('Result', thresh)
cv2.imwrite('output-'+name, thresh)
'''
