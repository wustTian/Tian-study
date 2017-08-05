#Filename:my_backup.py
def zip_dir(source,target_dir):
    '''此脚本用于将指定文件压缩到指定目录
    
    提供source要备份的文件目录和target_dir压缩目标目录
    还待优化
    '''
    version='0.1'
    
    import os
    import time

#1.需要备份的文件
#source=r'F:\测试'
#2.备份的存放目录
#target_dir=r'F:\Python学习资料'
#3.压缩后的文件名 

time1=time.strftime("%Y%m%d%H%M%S",time.localtime())
target='%s%s%s%s'%(target_dir,'\\',time1,'.zip')
print('备份文件目录:',target)

#zip_command="zip-qr %s %s"%(target,' '.join(source))
rar_command = r'"C:\Program Files\WinRAR\WinRAR.exe" a %s %s -r' % (target,source)
print('备份命令运行中\n',rar_command)

if os.system(rar_command)==0:
    print('文件成功备份至',target)
else:
    print('文件备份失败',target)
