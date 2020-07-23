#开发者:一只小菜鸟
#2020/7/15 1:04
#导入模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("https://www.baidu.com/")

ele = driver.find_element_by_id("kw")
ele.send_keys("selenium")
time.sleep(3)

#全选操作--ctrl + a
ele.send_keys(Keys.CONTROL,"a")
time.sleep(3)
#ctrl + x
ele.send_keys(Keys.CONTROL,"x")
time.sleep(3)
#ctrl + v
ele.send_keys(Keys.CONTROL,"v")
time.sleep(3)
#退格键
ele.send_keys(Keys.BACK_SPACE)
time.sleep(3)
#空格键
ele.send_keys(Keys.SPACE)
time.sleep(3)
#回车键
ele.send_keys(Keys.ENTER)
time.sleep(3)
#esc键
ele.send_keys(Keys.ESCAPE)
time.sleep(3)

