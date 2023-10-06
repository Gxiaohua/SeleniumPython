# -*- coding:utf-8 -*-
# 作者：郭晓华
# 时间：2022/9/27

from page.register_page import RegisterPage
class RegisterHandle(object):
    '''
    操作：
    根据页面中定位到元素来完成操作
    引入page模块
    '''
    def __init__(self,driver):
        # self.driver = driver
        self.register_p = RegisterPage(driver)

    #勾选checkbox
    def click_check_box(self):
        self.register_p.get_checkbox().click()
    #输入用户名
    def senf_sign_uesr_name(self,phone):
        self.register_p.get_sign_user_name().send_keys(phone)
    #输入密码
    def send_sign_password(self,password):
        self.register_p.get_sign_password().send_keys(password)
    #点击登录
    def click_login(self):
        self.register_p.get_login().click()
    #获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info == 'login_name_error':
                # 用户名为空错误信息
                text = self.register_p.get_name_error_element().text
            elif info == 'login_name_format_error':
                #用户名账号格式错误
                text = self.register_p.get_name_format_error().text
            elif info == 'login_password_error':
                # 密码为空-错误信息
                text = self.register_p.get_password_error_element().text
            elif info == 'do_login_error':
                # 用户名/密码输入错误
                text = self.register_p.get_do_login_error().text
            elif info == 'login_account_error':
                # 账号无法使用
                text = self.register_p.get_login_account_error().text
            else:
                 # 验证
                 text = self.register_p.get_slide().text
        except:
            text = None
        # print(text)
        return text





