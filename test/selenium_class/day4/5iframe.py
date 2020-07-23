#开发者:一只小菜鸟
#2020/7/15 12:17
#导入模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("D:\github\Project\\test\selenium_class\day4\\test3.html")

#定位到你想切换的标签
eleIframe = driver.find_element_by_css_selector("body > iframe:nth-child(3)")
#切换到这个内嵌网页
driver.switch_to.frame(eleIframe)
driver.find_element_by_id("kw").send_keys("abc")
#切回主页面
driver.switch_to.default_content()

