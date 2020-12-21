#开发者:一只小菜鸟
#2020/7/26 23:37
#导包
from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'6',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息:
    #adb shell dumpsys activity recents | findstr intent={
    'appPackage':'com.hpbr.bosszhipin',
    'appActivity':'.module.launcher.WelcomeActivity',
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
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#点击放大镜
eles=driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')#先取所有符合条件的元素
#找到第二个元素--放大镜
btn=eles[1]
btn.click()

#搜索框输入职位信息
search_input=driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
search_input.send_keys('软件测试')#输入参数

#选择符合条件的第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()
#点击搜索的第一个岗位
driver.find_element_by_id("com.hpbr.bosszhipin:id/view_job_card").click()
#获取  地区、工作年限、学历

region = driver.find_element_by_id("com.hpbr.bosszhipin:id/tv_required_location").text
job_age= driver.find_element_by_id("com.hpbr.bosszhipin:id/tv_required_work_exp").text
education = driver.find_element_by_id("com.hpbr.bosszhipin:id/tv_required_degree").text

print(f'地区: {region} 工作年限: {job_age} 学历: {education}')
driver.quit()