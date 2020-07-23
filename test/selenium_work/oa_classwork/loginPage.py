#开发者:一只小菜鸟
#2020/7/21 22:54
from test.selenium_work.oa_classwork.driver_address import Driver
class LoginPage:
    def __init__(self):
        # 创建driver对象
        self.driver = Driver.get_driver()
    #找到用户名输入框
    def userInput(self):
        return self.driver.find_element_by_name("username")
    #找到密码输入框
    def pwdInput(self):
        return self.driver.find_element_by_name("password")
    #找到登录按钮
    def loginButton(self):
        return self.driver.find_element_by_css_selector("button")

class LoginPageAction(LoginPage):

    def login(self):
        """登录系统"""
        # 输入用户名
        self.userInput().send_keys("libai")
        # 输入密码
        self.pwdInput().send_keys("opmsopms123")
        # 点击登录按钮
        self.loginButton().click()
if __name__ == "__main__":
    LoginPageAction().login()
