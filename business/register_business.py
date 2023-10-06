# -*- coding:utf-8 -*-
# 作者：郭晓华
# 时间：2022/9/27
import time

from selenium import webdriver
import sys
sys.path.append('D:\PythonProject\SeleniumPython\SeleniumPython')

from handle.register_handle import RegisterHandle
# driver = webdriver.Chrome()
# driver.get('https://mail.163.com/')
# # driver.maximize_window()
class RegisterBusiness(object):
    '''
    该类是页面+操作后形成的业务层
    eg：登录{
        1、定位元素
        2、操作
        3、元素+操作 一起完成登录
    }
    引入handle模块
    '''
    def __init__(self,driver):
        # self.driver = driver
        self.register_h = RegisterHandle(driver)

    #登录操作
    def base_login(self,phone,password):
        self.register_h.senf_sign_uesr_name(phone)
        self.register_h.send_sign_password(password)
        self.register_h.click_check_box()
        self.register_h.click_login()




    #点击登录按钮
    def login_bitton(self):
        self.register_h.click_login()

    #sigin_name_error
    def login_function(self,phone,password,assertCode,assertText):
        self.base_login(phone,password)
        time.sleep(3)
        if self.register_h.get_user_text(assertCode,assertText) == None:
            '''
            填写正确，登录成功 --- 检验不成功
            '''
            return True
        else:
            return False







# if __name__ == '__main__':
    # rb =RegisterBusiness(driver)
    # rb.base_login(15712584580,123445)
