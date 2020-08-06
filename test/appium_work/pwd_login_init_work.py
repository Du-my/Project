#开发者:一只小菜鸟
#2020/7/30 23:13
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
    #boss直聘-------------------------------------------------------
    # 'appPackage':'com.hpbr.bosszhipin',
    # 'appActivity':'.module.launcher.WelcomeActivity',
    #星巴克------------------------------------------------------
    'appPackage': 'com.tencent.mm',  # com.tencent.mm/.ui.LauncherUI星巴克小程序
    'appActivity': '.ui.LauncherUI',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName':'UiAutomator2',#或者UiAutomator1
    # 'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
}