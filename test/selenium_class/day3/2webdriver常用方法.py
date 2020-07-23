#开发者:一只小菜鸟
#2020/7/13 22:14
#导入模块
from selenium import webdriver
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("https://www.baidu.com/")
# ele = driver.find_element_by_id("kw")
# ele.send_keys("这是文本内容")
# time.sleep(3)
# ele.clear()
# ele.send_keys("selenium")
# ele.submit()

#获取元素的属性值
ele = driver.find_element_by_id("su")
#检测元素是否可见
print(ele.get_attribute("value"))
#检测元素是否可见
print(ele.is_displayed())
#获取元素的文本值
print(ele.text)
#返回元素的尺寸
print(ele.size)


