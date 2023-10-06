# -*- coding:utf-8 -*-
# 作者：郭晓华
# 时间：2022/9/28
from selenium import webdriver
from selenium.webdriver.common.by import By
class GetDriver(object):
    def __init__(self,index=None,url=None):
        if index == None:
            index = 0
        if url == None:
            self.url ='https://mail.163.com/'
        else:
            self.url = url
        self.driver = self.creat_driver(index)
    #生成driver
    def creat_driver(self,index):
        if index == 1:
            driver = webdriver.Ie()
        elif index == 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        return driver

    #打开浏览器
    def get_driver(self):
        self.driver.get(self.url)