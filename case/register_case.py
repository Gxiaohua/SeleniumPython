# -*- coding:utf-8 -*-
# 作者：郭晓华
# 时间：2022/9/29

import unittest
import ddt
import pytest
import time
import HTMLTestRunner
import sys
sys.path.append('D:\PythonProject\SeleniumPython\SeleniumPython')
from business.register_business import RegisterBusiness
from base.get_driver import GetDriver
from util.excel_util import ExcelUtil
from selenium import webdriver
import os
ex = ExcelUtil()
data = ex.get_change_value()
@ddt.ddt
class RegisterCase(unittest.TestCase):
    @classmethod
    # def setUpClass(cls):
    #     print('setUpClass')
    #     driver = webdriver.Chrome()
    #     driver.get('https://mail.163.com/')
    #     cls.register_b = RegisterBusiness(driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')

    def setUp(self):
        self.driver = GetDriver().get_driver()
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.163.com/')
        self.register_b = RegisterBusiness(self.driver)
        print('开始启动')
    def tearDown(self):
        self.driver.close()
        print('结束喽')


    @ddt.data(*data)
    def test_register_case(self,data):
        phone,password,assertCode,assertText = data
        print(data)
        login_error = self.register_b.login_function(phone,password,assertCode,assertText)
        self.assertFalse(login_error,'测试失败')

if __name__ == '__main__':
    unittest.main()
    # path = os.getcwd()
    # file_path = os.path.join(os.path.dirname(path) + "\\report\\" + 'reegister_case.html')
    # with open(file_path,'wb') as f:
    #    suite = unittest.TestLoader().loadTestsFromTestCase(RegisterCase)
    #    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="reegister_case", description=u"登录验证信息", verbosity=2)
    #    runner.run(suite)







