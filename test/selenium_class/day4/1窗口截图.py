#开发者:一只小菜鸟
#2020/7/14 23:36
#导入模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("https://www.baidu.com/")
#截取整个界面
driver.get_screenshot_as_file("./all.png")
#截取单个元素
ele = driver.find_element_by_id("form")
ele.screenshot("./ele.png")

driver.quit()



