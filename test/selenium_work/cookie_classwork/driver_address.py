#开发者:一只小菜鸟
#2020/7/21 22:52
from selenium import webdriver
from test.selenium_work.oa_classwork.settings import url, driverPath
class Driver:
    _driver = None
    @classmethod
    def get_driver(cls, browser_name="Chrome"):
        if cls._driver is None:
            if browser_name=="Chrome":
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
        # 访问默认网页
        cls._driver.get(url)
        return cls._driver

if __name__ =="__main__":
    Driver.get_driver()