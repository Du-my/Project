#开发者:一只小菜鸟
#2020/7/15 12:37
#导入模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("https://www.baidu.com/")
driver.implicitly_wait(5)
driver.find_element_by_css_selector(".title-text").click()
# 获取当前所有打开的标签页句柄
all_handles = driver.window_handles
# print(all_handles)
driver.switch_to.window(all_handles[1])
for handle in all_handles:
    driver.switch_to.window(handle)

    if driver.title == "百度搜索风云榜":
        break

print(driver.title)
# 点击小说
driver.find_element_by_css_selector("#main-nav > li:nth-child(4) > a").click()

