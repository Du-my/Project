#开发者:一只小菜鸟
#2020/8/4 22:35
#导包
from appium import webdriver
import time
print('-----启动')
#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'6',
    #设备的名称--值可以随便写
    'deviceName':'test',
    #提供被测app的信息-包名，入口信息:
    #adb shell dumpsys activity recents | findstr intent={
    'appPackage':'com.tencent.mm',#com.tencent.mm/.ui.LauncherUI星巴克小程序
    'appActivity':'.ui.LauncherUI',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName':'UiAutomator2',#或者UiAutomator1
    # 'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
}

#初始化driver对象-用于控制手机-启动被测应用
#IP-appium-server所在机器的网络ip，port-监听的端口号，path固定/wd/hub
print('准备打开程序')
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
print('连接上了')
driver.implicitly_wait(15)#稳定元素

# 先等待目标页面出现
driver.find_element_by_xpath('//*[@text="微信"]')
print('马上下拉')
#下拉
size = driver.get_window_size()
pos_x=size['width']/2
pos_y=size['height']/4
distance=size['height']/2
driver.swipe(pos_x, pos_y, pos_x, pos_y + distance)

#点击搜索框
driver.find_element_by_id("com.tencent.mm:id/rq").click()
# time.sleep(1)
#输入框搜索星巴克
driver.find_element_by_id('com.tencent.mm:id/m7').send_keys('星巴克')
# time.sleep(1)

#点击搜索结果
driver.find_element_by_xpath('//*[@resource-id="app"]//android.view.View[@text="星巴克用星说"]').click()
time.sleep(5)
#点击请TA喝咖啡
driver.find_element_by_xpath('//*[@text="请TA喝咖啡"]').click()

#等待进入购买商品页面
driver.find_element_by_xpath('//*[@text="购买礼物"]')
driver.implicitly_wait(0.5)
distance2=size['height']/4
while 1:
    # 滑动寻找美式咖啡
    eles = driver.find_elements_by_xpath('//*[@text="美式咖啡"]')
    if eles:
        print('找到咖啡后')
        driver.find_element_by_xpath('//*[@text="美式咖啡"]/../../following-sibling::android.view.View').click()
        print('点击+号数量+1')
        break
    driver.swipe(pos_x, pos_y+distance2, pos_x, pos_y)
driver.implicitly_wait(15)
#检查商品对应购物篮数字
goods_num = driver.find_element_by_xpath('//*[@text="美式咖啡"]/../../following-sibling::android.view.View/android.view.View/*/*').text
print('当前商品数量：%s'%goods_num)
#点击购买商品
driver.find_element_by_xpath('//*[@text="购买礼物"]').click()

#选择支付方式
# driver.find_element_by_xpath('//*[@text="选择支付方式"]')
# driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/dci"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]')
print('运行结束了')


