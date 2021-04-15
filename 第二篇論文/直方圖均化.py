# -*- coding: utf-8 -*-
import PIL
import PIL.Image
import numpy
def histogram_transformation(source,result):	#定義一個histogram轉換的函數
	if __name__ == "__main__":						#輸入圖片
		image = PIL.Image.open(source)
	width = image.width								#寬
	height = image.height							#高
	r=[]											#宣告原始histogram
	g=[]
	b=[]
	r2=[]											#宣告轉換histogram
	g2=[]
	b2=[]
	sumr=0											#宣告三色總和
	sumg=0
	sumb=0	
	color=1											#宣告變數紀錄灰階還是彩色
	grey=[]											#宣告灰階原始histogram
	grey2=[]										#宣告灰階轉換histogram
	sumgrey=0										#宣告灰階總和
	pixel=image.getpixel((0,0))
	try:											#判斷是不是彩色
		pixel[1]
		color=1
	except :										#如果不是彩色就判斷是灰階
		color=0		
	for i in range(256):							#初始化原始histogram和轉換histogram
		r.append(0)
		g.append(0)
		b.append(0)
		r2.append(0)
		g2.append(0)
		b2.append(0)
		grey.append(0)
		grey2.append(0)
	if color==1:									#-----------彩色的情況------------
		for col in range(width):						#得到轉換前的histogram
			for row in range(height):			
				pixel = image.getpixel((col,row))
				r[pixel[0]]+=1
				g[pixel[1]]+=1
				b[pixel[2]]+=1
		size = width * height							#算出照片大小
		for i in range(256):							#得到轉換後的histogram(累積機率函數)
			sumr=sumr+r[i]
			sumg=sumg+g[i]
			sumb=sumb+b[i]
			r2[i]=255*sumr//size
			g2[i]=255*sumg//size
			b2[i]=255*sumb//size
		for col in range(width):						#將原始圖依據轉換histogram進行轉換
			for row in range(height):
				pixel = image.getpixel((col,row))
				image.putpixel((col,row),(r2[pixel[0]],g2[pixel[1]],b2[pixel[2]]))
		image.save(result)								#存成新圖片
	else:											#-----------灰階的情況------------
		for col in range(width):						#得到轉換前的histogram
			for row in range(height):			
				pixel = image.getpixel((col,row))
				grey[pixel]+=1
		size = width * height							#算出照片大小
		for i in range(256):							#得到轉換後的histogram(累積機率函數)
			sumgrey=sumgrey+grey[i]
			grey2[i]=255*sumgrey//size
		for col in range(width):						#將原始圖依據轉換histogram進行轉換
			for row in range(height):
				pixel = image.getpixel((col,row))
				image.putpixel((col,row),grey2[pixel])
		image.save(result)								#存成新圖片
'''
histogram_transformation("01-1before-HE-Hwakes Bay.bmp","01-1after-HE-Hwakes Bay.bmp")								#依序將七張圖進行轉換
histogram_transformation("02-1before-HE-River.bmp","02-1after-HE-River.bmp")
histogram_transformation("03-1before-HE-Castle.bmp","03-1after-HE-Castle.bmp")
histogram_transformation("04-1before-HE-snow.bmp","04-1after-HE-snow.bmp")
histogram_transformation("05-1before-HE-stegosaurus.bmp","05-1after-HE-stegosaurus.bmp")
histogram_transformation("06-1before-HE-bird_of_paradise_flower.bmp","06-1after-HE-bird_of_paradise_flower.bmp")
histogram_transformation("07-1before-HE-Alhambra9.bmp","07-1after-HE-Alhambra9.bmp")
'''
histogram_transformation(r"D:\108RE\研究\第二篇論文\BOWS_PNG-rename\重複影像\00005536.png",r"D:\108RE\研究\第二篇論文\BOWS_PNG-rename\重複影像\00005536-改.png")
histogram_transformation(r"D:\108RE\研究\第二篇論文\BOWS_PNG-rename\重複影像\00005537.png",r"D:\108RE\研究\第二篇論文\BOWS_PNG-rename\重複影像\00005537-改.png")
histogram_transformation(r"D:\108RE\研究\第二篇論文\BOWS_PNG-rename\重複影像\00005538.png",r"D:\108RE\研究\第二篇論文\BOWS_PNG-rename\重複影像\00005538-改.png")
histogram_transformation(r"D:\108RE\研究\第二篇論文\BOWS_PNG-rename\重複影像\00005539.png",r"D:\108RE\研究\第二篇論文\BOWS_PNG-rename\重複影像\00005539-改.png")