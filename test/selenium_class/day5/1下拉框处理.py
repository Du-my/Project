#开发者:一只小菜鸟
#2020/7/17 9:15
#导入模块
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("D:\github\Project\\test\selenium_class\day5\\test.html")
ele = driver.find_element_by_id("abc")
# Select(ele).select_by_value("p2")
# Select(ele).select_by_index(3)
Select(ele).select_by_visible_text("月薪三十万")