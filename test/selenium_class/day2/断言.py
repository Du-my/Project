#作者:老杜
#2020/7/10
#导入模块
from selenium import webdriver
import unittest
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")

# class Atest(unittest.TestCase):
#     def test_title(self):
#         self.assertEqual(driver.title,"百度一下，你就知道")

driver.get("https://www.baidu.com/")
assert driver.title=="百度一下，你就知道"

#获取当前页面URL
print(driver.current_url)
assert driver.current_url=="https://www.baidu.com/"
#获取标签对之间的文本信息
time.sleep(2)
ele = driver.find_element_by_css_selector("#hotsearch-content-wrapper > li:nth-child(1) > a > span.title-content-title")
assert ele.text == "长江中下游各江段将迎洪峰"

driver.quit()
