#开发者:一只小菜鸟
#2020/7/17 9:25
#导入模块
from selenium import webdriver
import win32com.client
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("http://tinypng.com/")
#触发文件上传的操作
driver.find_element_by_css_selector(".icon").click()
sh = win32com.client.Dispatch("WScript.shell")
time.sleep(3)
sh.Sendkeys("D:\github\Project\\test\selenium_class\day5\\tea.png\n")


