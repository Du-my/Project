#开发者:一只小菜鸟
#2020/7/17 10:23
#导入模块
from selenium import webdriver
import win32com.client
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("http://127.0.0.1:8088/login")
#获得所有cookie信息
print(driver.get_cookies())
# 输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 点击登录按钮
driver.find_element_by_css_selector("button").click()
#获得所有cookie信息
print(driver.get_cookies())