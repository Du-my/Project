#开发者:一只小菜鸟
#2020/7/17 14:06
'''
登录页面，页面类
'''
#导入模块
from selenium import webdriver
#创建浏览器驱动对象
#访问网址

class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome("D:\\ruanjian\chromedriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8088/login")

        self.userInBox = self.driver.find_element_by_name("username")
        self.pwdInBox = self.driver.find_element_by_name("password")
        self.loginInBox = self.driver.find_element_by_css_selector("button")
    def login(self):
        self.userInBox.send_keys("libai")
        self.pwdInBox.send_keys("opmsopms123")
        self.loginInBox.click()
if __name__== "__main__":
    loginPageObj = LoginPage()
    loginPageObj.login()