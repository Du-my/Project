#开发者:一只小菜鸟
#2020/7/20 11:01
from selenium import webdriver
from test.selenium_class.day6.初级版本.mySetting import url, driverPath

class Driver:
    _driver = None
    @classmethod
    def get_driver(cls, browser_name="Chrome"):
        if cls._driver is None:
            if browser_name=="Chrome":
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
            #省略其他的浏览器类型

        #最大化窗口
        cls._driver.maximize_window()
        #访问默认网页
        cls._driver.get(url)
        return cls._driver

if __name__ =="__main__":
    Driver.get_driver()