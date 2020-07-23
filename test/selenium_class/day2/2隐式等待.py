#开发者:一只小菜鸟
#2020/7/13 13:57
from selenium import webdriver
import unittest
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")

# class Atest(unittest.TestCase):
#     def test_title(self):
#         self.assertEqual(driver.title,"百度一下，你就知道")

driver.implicitly_wait(20)

# 访问网址
driver.get("https://m.weibo.cn/")

ele = driver.find_element_by_css_selector(
    "#app > div.main-wrap > div.lite-topbar.main-top > div.nav-top > a > aside > label > div")
ele.click()

ele = driver.find_element_by_css_selector(
    "#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4")
ele.click()

ele = driver.find_element_by_css_selector(
    "#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(1) > div > div > div > div > span.main-link.m-box.m-box-center-a > span.main-text.m-text-cut")
print(ele.text)

# driver.quit()




