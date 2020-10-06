# -*- coding: utf-8 -*-
import tarfile
import os
def compress_zip(dir_folder,tar_name,file_name):
    cur_path = os.getcwd()  #儲存原本路徑
    os.chdir(dir_folder)    #移動到壓縮檔案的路徑
    with tarfile.open(tar_name, "w:gz") as tf:#依序加入要壓縮的檔案(因為gzip只能壓縮一個檔案，所以常和tar打包一起使用)
        tf.add(file_name)
    os.chdir(cur_path)#回到原本路徑
#compress_zip("./oneshoe1/output00000000","output00000000_location map.tar.gz","output00000000_location map.txt")
#compress_zip("./oneshoe1/output00000000","output00000000_lc.tar.gz","output00000000_lc.png")
for i in range(3):
    for j in range(20):
        name = "output{:08d}".format(j)
        compress_zip('./oneshoe'+str(i+1)+'/'+name,
                     name+'_location map.tar.gz',
                     name+'_location map.txt',)
        compress_zip('./oneshoe'+str(i+1)+'/'+name,
                     name+'_lc.tar.gz',
                     name+'_lc.png',)