#开发者:一只小菜鸟
#2020/8/2 18:01
import pytest
import time
from appium import webdriver
from config import boss_caps
def start_app():
    global driver
    driver=webdriver.Remote('http://localhost:4723/wd/hub',boss_caps)
    driver.implicitly_wait(10)
def change_psw(old_psw,new_psw):
    global driver
    # 1.进入我的标签
    driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_tab_4').click()
    # 2.点击右上角设置图标
    driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()
    # 3.进入账号与绑定
    driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item').click()
    time.sleep(1)
    # 4.进入设置密码
    driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/rv_list"]/*[2]/android.view.ViewGroup').click()
    # 5.完成密码设置
    #1.设置旧密码
    driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old').send_keys(old_psw)
    #2.输入新密码
    driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new').send_keys(new_psw)
    #3.确认新密码
    driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm').send_keys(new_psw)
    #4.保存修改
    driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()

    #检查首页信息
    ele=driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_password_login')
    assert ele.text=='账户密码登录'
def close_app():
    global driver
    driver.quit()
