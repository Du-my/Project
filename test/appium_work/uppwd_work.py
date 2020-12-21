#开发者:一只小菜鸟
#2020/7/30 17:51
#导包
from appium import webdriver

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

#先进入我的页面
driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_tab_4').click()
#点击设置进入设置详情页；
driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()
#点击账号与绑定
driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item').click()
#进入修改密码
driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/rv_list"]/android.widget.LinearLayout[2]/android.view.ViewGroup').click()
#输入旧密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old').send_keys('dw1996615.1314')
#设置新密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new').send_keys('dw19966152917')
#确认密码
driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm').send_keys('dw19966152917')
#点击修改密码按钮确认修改
driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()
print('---------------密码修改完成了------------------')
driver.quit()
