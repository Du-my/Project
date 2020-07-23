#开发者:一只小菜鸟
#2020/7/13 17:01
from selenium import webdriver

#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
driver.implicitly_wait(20)
# 访问网址
driver.get("https://m.weibo.cn/search?containerid=231583")

ele = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[3]/div/div/h4")
print(ele.text)

driver.quit()