# -*- coding:utf-8 -*-
# 作者：小花
# 时间：2022/9/26

# 读取config中int文件

import configparser
class ReadIni(object):
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = 'D:\PythonProject\SeleniumPython\SeleniumPython\config\LocalElement.int'
        if node == None:
            self.node = 'HomeElement'
        else:
            self.node = node

        self.cf = self.load_ini(file_name)

    #读取配置文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        #读取
        cf.read(file_name,encoding='UTF-8')
        # print(cf)
        return cf
    #获取配置文件中相对应内容
    def get_value(self,key):
        '''
        获取数据：
        第一步：先打开对应文件
        第二步：读取数据
        第三步：获取数据

        so：获取数据之前先调用读取数据的函数，读取数据的函数放到构造函数中先执行
        '''
        data = self.cf.get(self.node,key)
        # print(data)
        return data

if __name__ == '__main__':
   read_ini = ReadIni()
   print(read_ini.get_value('sigin_name'))
#
#
