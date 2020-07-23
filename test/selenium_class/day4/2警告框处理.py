#开发者:一只小菜鸟
#2020/7/15 0:10
#导入模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("file:///D:/github/Project/test/selenium_class/day4/test1.html")

# #触发对话框
# driver.find_element_by_id("bu1").click()
# #获取对话框
# al = driver.switch_to.alert
# al.accept()

# #触发提示框
# driver.find_element_by_id("bu2").click()
# # #获取确认框
# al = driver.switch_to.alert
# #取消提示框
# al.dismiss()

#触发提示
driver.find_element_by_id("bu3").click()
# #获取提示框
al = driver.switch_to.alert
al.send_keys("今天天气真好")
#取消提示框
al.accept()