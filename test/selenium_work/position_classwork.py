#开发者:一只小菜鸟
#2020/7/15 1:09
#导入模块
from selenium import webdriver
import time
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
#访问网址
driver.get("http://www.51job.com")
#隐式等待
driver.implicitly_wait(10)
#点击高级搜索
driver.find_element_by_css_selector("a.more").click()
#输入搜索关键字
driver.find_element_by_id("kwdselectid").send_keys("python")
#点击空白，取消搜索框下拉列表信息；
driver.find_element_by_css_selector(".rtit.r1").click()
#点击地区按钮
driver.find_element_by_id("work_position_input").click()
time.sleep(1)
#找到已选择地区展示控件
cityData =driver.find_element_by_id("work_position_click_multiple_selected")
#取消默认选中城市

cityData.find_elements_by_css_selector("span.ttag")[0].click()
# #找到杭州并点击
# driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
#找到北京并点击
driver.find_element_by_id("work_position_click_center_right_list_category_000000_010000").click()


#点击确认按钮
driver.find_element_by_id("work_position_click_bottom_save").click()
#点击空白，取消搜索框下拉列表信息；
driver.find_element_by_css_selector(".rtit.r1").click()
#找到职业类别并选择高级软件工程师
driver.find_element_by_id("funtype_click").click()
#找到后端开发并点击
driver.find_element_by_id("funtype_click_center_right_list_category_0100_0100").click()
#找到高级软件工程师并点击
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_0106").click()
#点击确认按钮
driver.find_element_by_id("funtype_click_bottom_save").click()

#公司选择外资，欧美
driver.find_element_by_css_selector("#cottype_list > input").click()
driver.find_element_by_css_selector("#cottype_list > div > span:nth-child(3)").click()

#展开下拉框
driver.find_element_by_css_selector("#workyear_list > input").click()
#选择条件1-3年
time.sleep(1)
driver.find_element_by_css_selector("#workyear_list > div > span:nth-child(3)").click()
#点击搜索按钮
driver.find_element_by_css_selector("div.btnbox > span.p_but").click()

#获取到职位列表
jobData = driver.find_elements_by_css_selector("#resultList > div.el")
for jobDataOne in jobData:
    if "title" in jobDataOne.get_attribute("class"):
        continue
    infoData = jobDataOne.find_elements_by_css_selector("span")
    for infoDataOne in infoData:
        print(infoDataOne.text)

driver.quit()




