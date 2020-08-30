#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,color,img_as_ubyte
def decode_mod(dir_code,dir_lc,dir_embed,dir_result,num_mod):
    f_code = open(dir_code,'r')
    f_lc= open(dir_lc,'r')
    f = open(dir_result,'w')
    image_embed = io.imread(dir_embed)
    count=0
    for row in range(image_embed.shape[0]):
        for col in range(image_embed.shape[1]):
            bit=f_lc.read(1)
            if bit== "0" or bit== "2" :
                for i in range(3):
                    a=image_embed[row][col][i]%num_mod
                    b=f_code.read(1)
                    f.write(str(a))
                    if a != int(b) :
                        count+=1
                    #print("{}".format(a)+"----{}".format(b))
    if count == 0 :
        print(dir_code+"-----------correct")
    else :
        print(dir_code+"-----------wrong!!!!!")
    f_code.close()
    f_lc.close()
    f.close()
'''
decode_mod('./oneshoe1/output00000000/output00000000_code.txt'
        ,'./oneshoe1/output00000000/output00000000_location map.txt'
        ,'./oneshoe1/output00000000/output00000000_embed.png'
        ,'./oneshoe1/output00000000/output00000000_decode.txt'
        ,5)
'''
for i in range(3):
    for j in range(20):
        name = "/output{:08d}".format(j)
        decode_mod('./oneshoe'+str(i+1)+name+name+'_code.txt'
                   ,'./oneshoe'+str(i+1)+name+name+'_location map.txt'
                   ,'./oneshoe'+str(i+1)+name+name+'_embed.png'
                   ,'./oneshoe'+str(i+1)+name+name+'_decode.txt'
                   ,5)                                                              #code-lc+embed+decode+mod
