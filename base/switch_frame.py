# -*- coding:utf-8 -*-
# 作者：郭晓华
# 时间：2022/9/28
from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.get("https://mail.163.com/")
class SwitchFrame(object):
    def __init__(self,driver):
        self.driver = driver
    def get_frame(self):
        '''
        切换到frame窗口
        1、先找frame，使用定位方法【id为动态数字时获取不到】
        2、切换
        '''
        frame = self.driver.find_elements(By.TAG_NAME,'iframe')[0]  #根据需要填入index，这里定位HTML里的第一个
        self.driver.switch_to.frame(frame)
        print('切换到frame',frame)



# if __name__ == '__main__':
    # sf = SwitchFrame(driver)
    # sf.get_driver()
    # sf.get_frame()
