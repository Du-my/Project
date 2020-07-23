#开发者:一只小菜鸟
#2020/7/20 16:49
from selenium import webdriver
from test.selenium_class.day7.utils.mySettings import url, driverPath

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
            cls.__login()
        return cls._driver

    @classmethod
    def __login(cls):
        #只在浏览器刚打开的时候登录一次
        cls._driver.find_element_by_name("username").send_keys("libai")
        cls._driver.find_element_by_name("password").send_keys("opmsopms123")
        cls._driver.find_element_by_css_selector("button").click()



if __name__ =="__main__":
    Driver.get_driver()