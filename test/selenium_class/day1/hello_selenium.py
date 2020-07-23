#作者:老杜
#2020/7/10
#导入模块
from selenium import webdriver
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("https://www.baidu.com/")
#找到搜索框
inpEle =driver.find_element_by_id("kw")
inpEle.send_keys("测试")
#找到搜索按钮
sEle = driver.find_element_by_id("su")
sEle.click()


#退出浏览器
# driver.quit()