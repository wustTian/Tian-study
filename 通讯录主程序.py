#Filename:通讯录主程序,py
#此程序为通讯录程序
#用于存储、修改、删除联系人信息
#设计：WUST_Tian
#开始时间：2017年8月12日
#完成时间：2017年8月16日
#版本：0.1
#完成了基本功能的搭建（添加，查询，修改，删除，备份）

import InformationSave
import 备份文件脚本 as b

print('欢迎使用通讯录\n开发者：WUST_T\n版本：0.1')
print('功能：\n1.添加联系人\n2.查询联系人信息\n3.查看联系人名单\n4.修改联系人信息\n5.删除联系人信息\n6.备份通讯录')

while True:
    answer=str(input('请输入功能编号：'))

    for case in InformationSave.switch(answer):
        if case('1'):
            #storage the data
            while True:
                name=str(input('请输入姓名(退出请输入0)：'))
                if name!='0':
                    Class=str(input('请输入联系人分类（同学、朋友、亲人或其他）：'))
                    phone=str(input('请输入联系人联系电话：'))
                    QQ=str(input('请输入联系人的QQ：'))
                    storagename=InformationSave.Information(name)
                    storagename.storage(name,Class,phone,QQ)
                else:
                    break
            break
        
        if case('2'):
            #look for one's data
            flag=True
            while flag:
                name=str(input('请输入要查询的联系人姓名(退出请输入0):'))
                lookname=InformationSave.Information(name)
                flag=lookname.lookfor(name)
            break

        if case('3'):
            #print the list
            InformationSave.Print()
            break

        if case('4'):
            #change the data
            InformationSave.change()
            break
            
        if case('5'):
            #delete one's data
            InformationSave.Del()

        if case('6'):
            b.savefile()
