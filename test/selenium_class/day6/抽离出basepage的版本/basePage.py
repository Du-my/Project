#开发者:一只小菜鸟
#2020/7/20 13:57
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.selenium_class.day6.抽离出basepage的版本.mySettings import TIMEOUT,POLL_FREQUENCY
from test.selenium_class.day6.抽离出basepage的版本.myDriver import Driver
class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()
        #根据表达式匹配单个元素，并返回元素对象
    def get_element(self,locator):
        WebDriverWait(
            driver=self.driver,
            timeout=TIMEOUT,
            poll_frequency=POLL_FREQUENCY
        ).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def get_elements(self,locator):
        WebDriverWait(
            driver=self.driver,
            timeout=TIMEOUT,
            poll_frequency=POLL_FREQUENCY
        ).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)