#开发者:一只小菜鸟
#2020/7/14 0:06
#导入模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("https://www.vmall.com/")
#隐式等待十秒
driver.implicitly_wait(10)
#获取所有的一级菜单
listData = driver.find_elements_by_css_selector("ol.category-list > li")
#遍历所有的一级菜单
for oneList in listData:
    #打印一级菜单文本内容
    print("一级菜单: ",oneList.find_element_by_css_selector("a >span").text)
    #鼠标悬停在一级菜单
    ActionChains(driver).move_to_element(oneList).perform()
    #匹配每一个二级菜单
    listData2 = oneList.find_elements_by_css_selector("li.subcate-item")
    for list2 in listData2:
        print("\t",list2.text)
print("-------------------------------------")
#找到热销单品中的每个单品
listHot = driver.find_elements_by_css_selector(".span-968.fl > ul.grid-list.clearfix >li")
#循环遍历列表
for oneListHot in listHot:
    #如果没有找到带标签的单品就继续找
    if not oneListHot.find_elements_by_css_selector("span"):
        continue
    #找到单品中有标签的获取其内容信息
    goodName = oneListHot.find_element_by_css_selector("div").text
    goodPrice = oneListHot.find_element_by_css_selector("p.grid-price").text
    goodType = oneListHot.find_element_by_css_selector("span").text
    #打印输出结果
    print("{}: {}, 价格: {}".format(goodType,goodName,goodPrice))
#关闭浏览器
driver.quit()


