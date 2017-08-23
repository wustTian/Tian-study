#Filename:InformationSave.py
#这是一个通讯录程序下的信息存储模块
#用于存储姓名,分类，电话号码，QQ等信息
#设计：WUST_Tian
#开始时间：2017年8月12日
#完成时间：未知
#版本：0.1

import os
import time
import pickle
import sys

version=0.1

class Information:
    total=0
    addresslist={}

    def __init__(self,name):
        '''initializes the people's data'''
        self.name=name

    def storage(self,name,classify,phone,icq):
        '''storage one's data'''
        self.classify=classify
        self.phone=phone
        self.icq=icq
        
        print('正在存储%s的信息'%self.name)
        f=open('通讯录.txt','wb')
        
        address=[self.classify,self.phone,self.icq]
        Information.addresslist[self.name]=address
        pickle.dump(Information.addresslist,f)
        f.close()

        time.sleep(1)
        print("已完成%s的信息存储\n"%name)
        Information.total+=1
    
    def lookfor(self,name):
        '''look for one's data'''
        f=open('通讯录.txt','rb')
        addresslist=pickle.load(f)
        while True:
            if name in addresslist:
                address=addresslist[name]
                print('姓名：%s'%name)
                print('分类：%s'%address[0])
                print('联系电话：%s'%address[1])
                print('QQ：%s\n'%address[2])
                return True
            else:
                if name=='0':
                    return False
                else:
                    print('查无此人，请重新确认姓名')
                    return True

def change():
    '''change the address information'''
    f=open('通讯录.txt','rb')
    addresslist=pickle.load(f)
    f.close()
    f=open('通讯录.txt','wb')
    while True:
        name1=str(input('请输入要修改信息的联系人姓名：(退出请输入0)'))
        if name1 in addresslist:
            address=addresslist[name1]
                
            print('姓名：%s'%name1)
            print('分类：%s'%address[0])
            print('联系电话：%s'%address[1])
            print('QQ：%s\n'%address[2])

            while True:
                choice=str(input('请输入要修改的信息：（姓名、分类、联系电话、QQ，退出请输入0）'))
                if choice=='0':
                    break
                else:
                    for case in switch(choice):
                        if case('姓名'):
                            name2=str(input('请输入新的姓名：'))
                            print('正在修改联系人姓名...')
                            del addresslist[name1]
                            addresslist[name2]=address
                            print('修改后的信息为：')
                            print('姓名：%s'%name2)
                            print('分类：%s'%address[0])
                            print('联系电话：%s'%address[1])
                            print('QQ：%s\n'%address[2])
                            pickle.dump(addresslist,f)
                            break
                        if case ('分类'):
                            Class2=str(input('请输入新的分类：'))
                            print('正在修改联系人分类...')
                            address[0]=Class2
                            addresslist[name1]=address
                            print('修改后的信息为：')
                            print('姓名：%s'%name1)
                            print('分类：%s'%address[0])
                            print('联系电话：%s'%address[1])
                            print('QQ：%s\n'%address[2])
                            pickle.dump(addresslist,f)
                            break
                        if case ('联系电话'):
                            Phone2=str(input('请输入新的联系电话：'))
                            print('正在修改联系人电话...')
                            address[1]=Phone2
                            addresslist[name1]=address
                            print('修改后的信息为：')
                            print('姓名：%s'%name1)
                            print('分类：%s'%address[0])
                            print('联系电话：%s'%address[1])
                            print('QQ：%s\n'%address[2])
                            pickle.dump(addresslist,f)
                            break
                        if case ('QQ'):
                            QQ2=str(input('请输入新的QQ：'))
                            print('正在修改联系人QQ...')
                            address[2]=QQ2
                            addresslist[name1]=address
                            print('修改后的信息为：')
                            print('姓名：%s'%name1)
                            print('分类：%s'%address[0])
                            print('联系电话：%s'%address[1])
                            print('QQ：%s\n'%address[2])
                            pickle.dump(addresslist,f)
                            break
                        if case():
                            print('请重新输入')
        else:
            if name1=='0':
                break
                f.close()
            else:
                print('查无此人，请重新确定联系人姓名！')
                time.sleep(1)

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False
    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: 
            self.fall = True
            return True
        else:
            return False

def Print():
    '''print the addresslist'''
    print('正在读取通讯录联系人信息...')
    f=open('通讯录.txt','rb')
    size=os.path.getsize('通讯录.txt')
    if size!=0:
        addresslist=pickle.load(f)
        for name in addresslist:
            address=addresslist[name]
            if len(name)<3:
                print('姓名:%s  '%name,end='　')
            else:
                print('姓名:%s'%name,end='　')

            print('分类：%-3s 联系电话：%-11s QQ：%-12s'%(address[0],address[1],address[2]))
        print('通讯录联系人信息打印完成')
        f.close()
    else:
        print('通讯录信息为空，请先存储联系人信息')
        f.close()

def Del():
    '''Delete one's data'''
    f=open('通讯录.txt','rb')
    addresslist=pickle.load(f)
    f.close()
    f=open('通讯录.txt','wb')
    while True: 
        name=str(input('请输入要删除的联系人姓名：(退出请输入0)'))
        if name=='0':
            break
        else:
            if name in addresslist:
                del addresslist[name]
                print('已删除%s的信息'%name)
                pickle.dump(addresslist,f)
            else:
                print('没有找到%s的信息,请重新确认姓名'%name)
    f.close()

