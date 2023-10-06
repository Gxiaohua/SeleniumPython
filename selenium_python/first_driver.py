# -*- coding:utf-8 -*-
# 作者：小花
# 时间：

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://mail.163.com/')
driver.maximize_window()
# driver.find_element()
# element = driver.find_element(By.ID,'js-signin-btn')
# element.click()
# # print(element)
# # e = driver.find_element(By.ID,'signup-form')
# # print(1)
# # driver.switch_to.frame('#signin')
# # driver.getWindowHandles()
# # element.click()
# # print(driver.switch_to.frame('signin'))
# locator = driver.find_element(By.CSS_SELECTOR,'input[name = "email"]')
# # //*[@id="signup-form"]/div[1]/input[@name='email']
# #signin
#
# all_handles = driver.window_handles
# driver.switch_to.window(all_handles[0])
# print(all_handles)
# # e =driver.find_elements(By.CLASS_NAME,'rl-modal')
# # ea =driver.find_elements(By.NAME,'email')
# # locator = (By.ID,'signup-form')
#
# # locator = (By.XPATH,'//*[@id="signup-form"]/div[1]/input[@name="email"]')
# # ec = driver.find_elements(By.CLASS_NAME,'rlf-group')
# WebDriverWait(driver,10).until(locator)
# # locator.get_attribute(value)
# # locator.send_keys(78979809)
checkbox = driver.find_element(By.XPATH,"xpath>//input[@type = 'checkbox' and @name = 'un-login']")
print(checkbox)

# print(element,locator)
# driver.find_element(By.ID, 'signup-form')



# driver.minimize_window()
driver.close()
