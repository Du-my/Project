#开发者:一只小菜鸟
#2020/7/13 22:05
#导入模块
from selenium import webdriver
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("https://www.baidu.com/")
driver.get("https://www.taobao.com/")
#浏览器后退
driver.back()
time.sleep(3)

#浏览器前进
driver.forward()
time.sleep(3)
#刷新页面
driver.refresh()
driver.set_window_size(700,700)
time.sleep(3)
#设置全屏展示
driver.maximize_window()
time.sleep(3)
#设置最小化
driver.minimize_window()
time.sleep(3)
#设置浏览器宽度与高度



