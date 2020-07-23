#开发者:一只小菜鸟
#2020/7/13 22:31
#导入模块
from selenium import webdriver
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("https://www.baidu.com/")
driver.find_element_by_css_selector("#kw").send_keys("12345")



