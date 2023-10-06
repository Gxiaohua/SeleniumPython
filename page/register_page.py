# -*- coding:utf-8 -*-
# 作者：郭晓华
# 时间：2022/9/27
import sys
sys.path.append('D:\PythonProject\SeleniumPython\SeleniumPython')
from base.find_element import FindElement
from base.switch_frame import SwitchFrame
from selenium import webdriver
import time
class RegisterPage(object):
    '''
    页面定位元素
    '''
    def __init__(self,driver):
        # self.driver = driver
        sf = SwitchFrame(driver)
        sf.get_frame()
        self.fd = FindElement(driver)
#   #获取用户名
    def get_sign_user_name(self):
        return self.fd.get_element('login_name')
    #获取密码
    def get_sign_password(self):
        return self.fd.get_element('login_password')
    #获取checkbox
    def get_checkbox(self):
        return self.fd.get_element('check_box')
    #获取登录按钮
    def get_login(self):
        return self.fd.get_element('do_login')
    #用户名为空错误信息
    def get_name_error_element(self):
        return self.fd.get_element('login_name_error')
    #用户名账号格式错误
    def get_name_format_error(self):
        return self.fd.get_element('login_name_format_error')
    #密码为空-错误信息
    def get_password_error_element(self):
        return self.fd.get_element('login_password_error')
    #用户名/密码输入错误
    def get_do_login_error(self):
        return self.fd.get_element('do_login_error')
    #账号无法使用
    def get_login_account_error(self):
        return self.fd.get_element('login_account_error')
    #验证
    def get_slide(self):
        return self.fd.get_element('slide_error')




