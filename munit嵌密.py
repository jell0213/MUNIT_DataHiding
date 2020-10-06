#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
import random
import PIL
random.seed(100)
def Embed(test):
	image = io.imread(test+"_color.png")
	image_edge = io.imread(test+"_edge.png")
	image_edge = color.gray2rgb(image_edge)
	location_map=[]
	for col in range(image.shape[0]):										#標記嵌密的地方，(255,0,0)為嵌密處，(0,0,0)為黑邊，(255,255,255)為白色不可嵌密處
		location_map.append([])												#location map 暫時先用來記錄rgb像素值
		for row in range(image.shape[1]):
			location_map[col].append([])
			if int(image_edge[col,row,0]) < 255/2 and int(image_edge[col,row,1]) < 255/2 and int(image_edge[col,row,2]) < 255/2: #255/2是用來清除不乾淨邊框的門檻值
				location_map[col][row]=[0,0,0]
			elif int(image[col,row,0]) == 255 and int(image[col,row,1]) == 255 and int(image[col,row,2]) == 255:
				location_map[col][row]=[255,255,255]
			else :
				location_map[col][row]=[255,0,0]
	image_lc = io.imread(test+"_color.png")									#標記嵌密的地方的圖
	for col in range(image_lc.shape[0]):
		for row in range(image_lc.shape[1]):
			image_lc[col,row] = location_map[col][row]
	io.imsave(test+'_lc.png',image_lc)
	image_embed = io.imread(test+"_color.png")
	for col in range(image_embed.shape[0]):									#嵌密
		for row in range(image_embed.shape[1]):
			if image_lc[col,row,0] == 255 and image_lc[col,row,1] == 0 and image_lc[col,row,2] == 0:
				bit = random.randint(0,1)
				image_embed[col,row,0]=image_embed[col,row,0]//2*2+bit
				bit = random.randint(0,1)
				image_embed[col,row,1]=image_embed[col,row,1]//2*2+bit
				bit = random.randint(0,1)
				image_embed[col,row,2]=image_embed[col,row,2]//2*2+bit
	io.imsave(test+'_embed.png',image_embed)
test = 'shoe2'
Embed(test)
