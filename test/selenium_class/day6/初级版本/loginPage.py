
#开发者:一只小菜鸟
#2020/7/20 12:00


from test.selenium_class.day6.初级版本.myDriver import Driver
class LoginPage:
    def __init__(self):
        # 创建driver对象
        self.driver = Driver.get_driver()

    def userInpBox(self):
        """实时获取用户名输入框"""
        return self.driver.find_element_by_name("username")

    def pwdInpBox(self):
        """实时获取密码输入框"""
        return self.driver.find_element_by_name("password")

    def loginButtonBox(self):
        """实时获取登录按钮"""
        return self.driver.find_element_by_css_selector("button")

#抽离出页面动作类，继承相应的页面类
class LoginPageAction(LoginPage):

    def login(self):
        """登录系统"""
        # 输入用户名
        self.userInpBox().send_keys("libai")
        # 输入密码
        self.pwdInpBox().send_keys("opmsopms123")
        # 点击登录按钮
        self.loginButtonBox().click()
# class ProjectPage:
#     def __init__(self):
#         # 创建driver对象
#         self.driver = Driver.get_driver()
if __name__ == "__main__":
    LoginPageAction().login()


