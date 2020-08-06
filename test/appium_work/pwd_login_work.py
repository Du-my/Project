#开发者:一只小菜鸟
#2020/7/30 21:06
#导包
from appium import webdriver
from pwd_login_init_work import desired_caps
#初始化
class Start_app():
    def __init__(self):

        # 初始化driver对象-用于控制手机-启动被测应用
        # IP-appium-server所在机器的网络ip，port-监听的端口号，path固定/wd/hub
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 稳定元素


    def test_change_and_login(self):
        self.old_pwd = input("请输入旧密码：")
        self.new_pwd = input("请输入新密码：")

    # 修改密码操作
    def change_pwd(self, old_pwd, new_pwd):
        # 先进入我的页面
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_tab_4').click()
        # 点击设置进入设置详情页；
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()
        # 点击账号与绑定
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item').click()
        # 进入修改密码
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.hpbr.bosszhipin:id/rv_list"]/android.widget.LinearLayout[2]/android.view.ViewGroup').click()
        # 输入旧密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old').send_keys(old_pwd)
        # 设置新密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new').send_keys(new_pwd)
        # 确认密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm').send_keys(new_pwd)
        # 点击修改密码按钮确认修改
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()
        print('---------------密码修改完成了------------------')

    # 实现登录流程
    def login(self,pwd):
        # 点击密码登录
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_password_login').click()
        # 输入密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_password').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_login').click()

        # 检查登录
        title = self.driver.find_element_by_xpath(
            '//*[@resource-id="com.hpbr.bosszhipin:id/scroll_view"]//android.widget.TextView').text
        # 校验标题
        if title == '软件测试':
            return True
        else:
            return False
    #关闭被测应用
    def close_app(self):
        self.driver.quit()



if __name__ == '__main__':
    startapp = Start_app()
    startapp.test_change_and_login()
    startapp.change_pwd(startapp.old_pwd,startapp.new_pwd)
    startapp.login(startapp.new_pwd)
