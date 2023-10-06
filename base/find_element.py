# -*- coding:utf-8 -*-
# 作者：郭晓华
# 时间：2022/9/27
from util.read_ini import ReadIni
from selenium.webdriver.common.by import By
class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
    '''
    定位元素信息封装：
    1、拿到*.ini文件中元素
    2、拆分定位元素
    3、不同的元素使用不同的定位方法，查找元素
    '''
    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element(By.ID, value)
                # return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element(By.NAME, value)
                # return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element(By.CLASS_NAME, value)
                # return self.driver.find_element_by_class_name(value)
            else:
                # print(1222,'xpath',value)
                return self.driver.find_element(By.XPATH, value)
                # return self.driver.find_element_by_xpath(value)
        except:
            return None


