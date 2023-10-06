# -*- coding:utf-8 -*-
# 作者：郭晓华
# 时间：2022/9/28
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://mail.163.com/")
driver.implicitly_wait(3)
iframe = driver.find_elements(By.TAG_NAME,"iframe")[0]   # 根据需要填入index，这里定位HTML里的第一个
driver.switch_to.frame(iframe)

# driver.switch_to.frame('x-URS-iframe1664348665883.669')
# user_name = driver.find_elements(By.TAG_NAME,"input")[0]
user_name = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email']")
password = driver.find_element(By.XPATH,"//input[@type = 'password' and @name = 'password']")
checkbox = driver.find_element(By.XPATH,"//input[@type = 'checkbox' and @name = 'un-login']")
# document.getElementsByClassName('ferrorhead')

login = driver.find_element(By.ID,'dologin')
login.click()
driver.implicitly_wait(5)
sigin_name_error=driver.find_element(By.XPATH,"//div[@id='nerror' and @class='m-nerror err_email']/div[text()='请输入帐号']")
user_name.send_keys('sdgdg')
password.send_keys('')
login.click()
# fer = driver.find_element(By.XPATH,"//div[@id='nerror' and @title='帐号或密码错误']/div[text()='帐号或密码错误']")
pa_error = driver.find_element(By.XPATH,"//div[@id='nerror' and @class='m-nerror err_password']/div[text()='请输入密码']")
# again_re = driver.find_element(By.XPATH,"//div[@id='nerror' and @title='该帐号无法使用，请重新注册其他帐号']/div[@class = 'ferrorhead']")
print(sigin_name_error,pa_error.text,password.text)

all_handles = driver.window_handles
# driver.switch_to.window(all_handles[0])
print(all_handles)
time.sleep(3)
driver.close()



