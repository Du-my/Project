#开发者:一只小菜鸟
#2020/7/15 0:36
#导入模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("https://www.baidu.com/")
ele = driver.find_element_by_name("tj_briicon")
#对定位的元素进行悬停操作
ActionChains(driver).move_to_element(ele).perform()
#对定位的元素进行右键操作
ActionChains(driver).context_click(ele).perform()
#双击
ActionChains(driver).double_click(ele).perform()

#访问网址
driver.get("D:\github\Project\\test\selenium_class\day4\\test2.html")
#定位要拖动的元素
ele1 = driver.find_element_by_id("blackSquare")
#定位到目标元素
ele2 = driver.find_element_by_id("targetEle")

ActionChains(driver).drag_and_drop(ele1,ele2).perform()