#开发者:一只小菜鸟
#2020/7/13 16:30
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#创建浏览器驱动对象
driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
# 访问网址
driver.get("https://m.weibo.cn/")

ele = driver.find_element_by_css_selector(
    "#app > div.main-wrap > div.lite-topbar.main-top > div.nav-top > a > aside > label > div")
ele.click()
ele = WebDriverWait(driver,10,0.5).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,"#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4")
    )
)
ele.click()

# ele = driver.find_element_by_css_selector(
#     "#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4")
# ele.click()
#
# ele = driver.find_element_by_css_selector(
#     "#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(1) > div > div > div > div > span.main-link.m-box.m-box-center-a > span.main-text.m-text-cut")
# print(ele.text)
