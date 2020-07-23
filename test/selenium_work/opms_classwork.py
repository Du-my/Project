#开发者:一只小菜鸟
#2020/7/17 16:29
from selenium import webdriver
import win32com.client
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("http://127.0.0.1:8088/login")
# 输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 点击登录按钮
driver.find_element_by_css_selector("button").click()
#点击项目管理
time.sleep(3)
driver.find_element_by_css_selector("div:nth-child(3)>ul>li:nth-child(2) span").click()
#点击新项目
time.sleep(3)
driver.find_element_by_css_selector("div > div.pull-right").click()
time.sleep(2)
#输入项目名称
driver.find_element_by_name("name").send_keys("作业项目")
time.sleep(2)

#输入项目别名
driver.find_element_by_name("aliasname").send_keys("作业别名")
#输入描述信息--->先切换iframe
time.sleep(3)
eleIframe = driver.find_element_by_css_selector(".ke-edit-iframe")
driver.switch_to.frame(eleIframe)
#输入描述
time.sleep(2)
driver.find_element_by_css_selector(".ke-content").send_keys("作业新建的项目描述")
#切换回主页面
driver.switch_to.default_content()
#点击提交
driver.find_element_by_css_selector("button.btn").click()
time.sleep(2)
#点击关闭弹框按钮；
driver.find_element_by_css_selector("button.close").click()
#关闭浏览器
driver.quit()