#开发者:一只小菜鸟
#2020/8/6 17:45
from appium import webdriver
import time
import pytest
from pwd_login_init_work import desired_caps

def open_session():
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print('连接上了')
    driver.implicitly_wait(15)  # 稳定元素

def close_session():
    global driver
    driver.quit()
#滑动距离为负数-向上滑动，反之向下滑动，起点为屏幕中心点
def swipe_screen(distance):
    size = driver.get_window_size()
    pos_x = size['width'] / 2
    pos_y = size['height'] / 2
    driver.swipe(pos_x, pos_y, pos_x, pos_y + distance)


#打开小程序
def open_miniprogram():
    global driver
    # 先等待目标页面出现
    driver.find_element_by_xpath('//*[@text="微信"]')
    print('马上下拉')
    # 下拉
    size = driver.get_window_size()
    # pos_x = size['width'] / 2
    # pos_y = size['height'] / 4
    distance = size['height'] / 2-10
    # 向下距离为正数
    swipe_screen(distance)
    # driver.swipe(pos_x, pos_y, pos_x, pos_y + distance)
    time.sleep(1)
    # 点击搜索框
    driver.find_element_by_id("com.tencent.mm:id/rq").click()
    # time.sleep(1)
    # 输入框搜索星巴克
    driver.find_element_by_id('com.tencent.mm:id/m7').send_keys('星巴克')
    # time.sleep(1)

    # 点击搜索结果
    driver.find_element_by_xpath('//*[@resource-id="app"]//android.view.View[@text="星巴克用星说"]').click()
    time.sleep(5)

#挑选商品+提交订单
def select_items():
    # 点击请TA喝咖啡
    driver.find_element_by_xpath('//*[@text="请TA喝咖啡"]').click()

    # 等待进入购买商品页面
    driver.find_element_by_xpath('//*[@text="购买礼物"]')
    driver.implicitly_wait(0.5)
    size = driver.get_window_size()
    distance2 = -500
    while 1:
        # 滑动寻找美式咖啡
        eles = driver.find_elements_by_xpath('//*[@text="美式咖啡"]')
        if eles:
            print('找到咖啡后')
            driver.find_element_by_xpath('//*[@text="美式咖啡"]/../../following-sibling::android.view.View').click()
            print('点击+号数量+1')
            break
        # driver.swipe(pos_x, pos_y + distance2, pos_x, pos_y)
        swipe_screen(distance2)
    driver.implicitly_wait(15)
    # 检查商品对应购物篮数字
    goods_num = driver.find_element_by_xpath(
        '//*[@text="美式咖啡"]/../../following-sibling::android.view.View/android.view.View/*/*').text
    print('当前商品数量：%s' % goods_num)
    # 点击购买商品
    driver.find_element_by_xpath('//*[@text="购买礼物"]').click()
def setup():
    open_session()
def teardown():
    close_session()
def test_miniprogram():
    open_miniprogram()
    select_items()
    # 选择支付方式
    # driver.find_element_by_xpath('//*[@text="选择支付方式"]')
    # driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/dci"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]')

if __name__ == '__main__':
    pytest.main(['xcx_fengzhuang.py','-s'])






