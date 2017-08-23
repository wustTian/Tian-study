#Filename:my_backup.py
#def zip_dir(source,target_dir):
#    '''此脚本用于将指定文件压缩到指定目录
#    
#    提供source要备份的文件目录和target_dir压缩目标目录
#    还待优化    '''
#    version='0.1'
    
import os
import time

def savefile() :
    #1.需要备份的文件
    source=r'F:\Vistual_Studio工程文件\Visual_Studio\project\PythonApplication1\PythonApplication1\通讯录.txt'

    #2.备份的存放目录
    target_dir=r'F:\Vistual_Studio工程文件\Visual_Studio\project\PythonApplication1\PythonApplication1\通讯录备份'

    #3.压缩后的文件名 
    time1=time.strftime("%Y%m%d%H%M%S",time.localtime())
    target='%s\\%s%s'%(target_dir,time1,'.zip')
#   print('备份文件目录:',target)

    rar_command = r'"C:\Program Files\WinRAR\WinRAR.exe" a %s %s -r' % (target,source)
#    print('备份命令运行中\n',rar_command)
    print('正在备份通讯录...')
    if os.system(rar_command)==0:
        print('通讯录成功备份至',target)
    else:
        print('通讯录备份失败',target)
