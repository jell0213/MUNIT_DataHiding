# -*- coding: utf-8 -*-
import math
from os.path import join
from openpyxl import Workbook
def base_analyze(maxln,n):    
    loss_ratio = 1 #初始化損失比率的值
    for ln in range(1,maxln+1):
        l2 = int(ln*math.log(n,2)//1)  #對應的S2長度
        bit = 100000000 #要取到小數第幾位
        power_n = pow(n,ln)*bit
        power_2 = pow(2,l2)
        result = power_n//power_2/bit-1
        if result < loss_ratio :
            loss_ratio = result
            num_ln = ln
            num_l2 = l2
    return n, num_ln, num_l2, loss_ratio, maxln
def print_base_analyze(x):
    print("{0}進制".format(x[0]))
    print("ln = "+str(x[1]))
    print("l2 = "+str(x[2]))
    print("loss_ratio = {:.8f}".format(x[3]))
def print_base_analyze_excel(x,path):
    #mypath=str(input("請輸入路徑"))#資料夾路徑      
    path_excel = join(path,"進制轉換分析.xlsx")
    if not(path_excel) :
        wb = Workbook()
        ws = wb.active
        ws.append(["E = {0}".format(x[4])])
        ws.append("進制", "Ln", "L2", "轉換損失比率")
        wb.save(path_excel)
    wb = Workbook()
    ws = wb.active
    ws.append(["E = {0}".format(x[4])])
    ws.append("進制", "Ln", "L2", "轉換損失比率")
    ws.append([x[0],x[1],x[2],x[3]])
    wb.save(path_excel)
#主程式  
maxln = 25035 #設定最長可嵌密數
for n in range(3,9):
    print_base_analyze(base_analyze(maxln,n))