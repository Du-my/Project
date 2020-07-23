#作者:老杜
#2020/7/10
from selenium.webdriver.common.by import By
from selenium import webdriver
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("file:///D:/github/Project/test/selenium_class/day1/test.html")

#第一种通过Id进行定位，只返回匹配的第一个元素找不到就报错
# txtEle = driver.find_element_by_id("abc")
# print(txtEle.text)
#第二种通过name定位，找不到就报错
# txtEle = driver.find_element_by_name("a1").send_keys("我的乖乖")
# #第三种通过xpath定位,只返回匹配的第一个元素找不到就报错
# ele = driver.find_element_by_xpath("/html/body/div[1]/select/option[3]")
# print(ele.text)
# #第四种根据css表达式定位,只返回匹配的第一个元素找不到就报错
# ele = driver.find_element_by_css_selector("body > div:nth-child(3) > select > option:nth-child(3)")
# print(ele.text)
#第五种根据链接文本定位,只返回匹配的第一个元素找不到就报错
# driver.find_element_by_link_text("访问百度").click()
#模糊查询
# driver.find_element_by_partial_link_text("百度").click()
#根据tag_name定位，只返回匹配的第一个元素找不到就报错
# ele = driver.find_element_by_tag_name("span")
# print(ele.text)
#根据class属性定位
# ele = driver.find_element_by_class_name("a2")
# print(ele.text)
#匹配元素列表，返回所有匹配到的元素，一个都匹配不到返回空列表
# ele = driver.find_elements_by_tag_name("span")
# for i in ele:
#     print(i.text)
ele = driver.find_element(By.TAG_NAME,"span")
print(ele.text)
# driver.quit()
