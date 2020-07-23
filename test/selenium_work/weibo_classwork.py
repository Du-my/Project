#作者:一只小菜鸟
#2020/7/10
#导入模块
from selenium import webdriver
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址：
driver.get("https://m.weibo.cn/")
#点击大家都在搜
driver.find_element_by_class_name("m-font.m-font-search").click()
time.sleep(1)
#找到微博热搜榜
#先找到整个大家都在搜模块
hotSearchEle = driver.find_element_by_class_name("card.m-panel.card16.m-col-2")
#再找到大家都在搜中的每条数据
hotSearchSli = hotSearchEle.find_elements_by_class_name("m-item-box")
hotSearchSli[-1].click()
time.sleep(1)
#先找到实时热点的大标签；
hotList = driver.find_element_by_css_selector("#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
#再找到热点列表中的每条数据
oneList = driver.find_elements_by_class_name("card.m-panel.card4")
#遍历列表数据判断数据类型
for one in oneList:
    #先找到图标，判断有数据的图标时再进行下一步判断
    icon = one.find_elements_by_class_name("m-link-icon")
    if icon:
        img = icon[0].find_element_by_tag_name("img")
        src = img.get_attribute("src")#获取图片路径数据
        if "hot.png" in src:
            listType = "最热"
            listText =one.find_element_by_class_name("main-text.m-text-cut").text
            print("{}:{}".format(listType,listText))
        elif "new.png" in src:
            listType = "最新"
            listText = one.find_element_by_class_name("main-text.m-text-cut").text
            print("{}:{}".format(listType, listText))
        elif "fei.png" in src:
            listType = "沸"
            listText = one.find_element_by_class_name("main-text.m-text-cut").text
            print("{}:{}".format(listType, listText))
#关闭浏览器
driver.quit()



