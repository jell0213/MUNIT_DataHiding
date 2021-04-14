<<<<<<< HEAD
# -*- coding: utf-8 -*-
import xlrd
from collections import Counter
def find_same_xls(xls_path,col_num) :
    data = xlrd.open_workbook(xls_path,col_num)
    table = data.sheets()[0]#指定sheet0
    lst =  table.col_values(col_num-1)
    set_lst=set(lst)
    if len(set_lst)==len(lst):
        print('沒重複。')

    else:
        print('有重複！')
    #print(table.col_values(col_num-1))#指定列之某值
    #print(table.nrows)
    result = Counter(lst)
    most_common = result.most_common()
    count=0
    for i in range(len(most_common)):
        if most_common[i][1] > 1:
            print(most_common[i])
            count+=1
    print("重複組數 =",count,"組")
    '''
    count = 0 
    time = 0 
    for i in range(table.nrows-1):
        for j in range(table.nrows-1-i-1):
            time+=1
            a = table.col_values(col_num-1)[i+1]
            b = table.col_values(col_num-1)[table.nrows-1-j]
            if a == b :
                count += 1
                print("{:08d}".format(i)+"----{:08d}".format(table.nrows-1-j-1))
    
    print("time =",time)            
    print("count =",count)
    '''
#xls_path=r'D:\108RE\第二篇論文\BOWS_PNG-rename\ENIQA結果-all.xls'
#xls_path=r'D:\108RE\第二篇論文\BOWS_PNG-rename\BRISQUE結果-all.xls'
xls_path=r'D:\108RE\第二篇論文\BOWS_PNG-rename\BOWS_PNG1000064-64\IQA_Color_Result_By_WSC.xls'
col_num=10
find_same_xls(xls_path,col_num)
=======
# -*- coding: utf-8 -*-
import xlrd
from collections import Counter
def find_same_xls(xls_path,col_num) :
    data = xlrd.open_workbook(xls_path,col_num)
    table = data.sheets()[0]#指定sheet0
    lst =  table.col_values(col_num-1)
    set_lst=set(lst)
    if len(set_lst)==len(lst):
        print('沒重複。')

    else:
        print('有重複！')
    #print(table.col_values(col_num-1))#指定列之某值
    #print(table.nrows)
    result = Counter(lst)
    most_common = result.most_common()
    
    for i in range(len(most_common)):
        if most_common[i][1] > 1:
            print(most_common[i])
    '''
    count = 0
    time = 0 
    for i in range(table.nrows-1):
        for j in range(table.nrows-1-i-1):
            time+=1
            a = table.col_values(col_num-1)[i+1]
            b = table.col_values(col_num-1)[table.nrows-1-j]
            if a == b :
                count += 1
                print("{:08d}".format(i)+"----{:08d}".format(table.nrows-1-j-1))
    
    print("time =",time)            
    print("count =",count)
    '''
xls_path=r'D:\108RE\第二篇論文\BOWS_PNG\BOWS_PNG10000\IQA_Color_Result_By_WSC.csv'
col_num=2
find_same_xls(xls_path,col_num)
>>>>>>> 626064154e3f93f41a487db1b25eef2ea9e15c63
