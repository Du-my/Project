#开发者:一只小菜鸟
#2020/7/21 22:54
from test.selenium_work.oa_classwork.driver_address import Driver
driver = Driver.get_driver()
cookieSli = [{'domain': '127.0.0.1',
              'httpOnly': False,
              'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
              'path': '/',
              'secure': False,
              'value': '1594957359'},
             {'domain': '127.0.0.1',
              # 'expiry': 1626493358,
              'httpOnly': False,
              'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
              'path': '/',
              'secure': False, 'value': '1594957359'},
             {'domain': '127.0.0.1',
              # 'expiry': 1626493357,
              'httpOnly': True,
              'name': 'beegosessionID',
              'path': '/',
              'secure': False,
              'value': 'd362fcc6a55847a47fb9b5d8326779d1'}]
#先清除所有cookie
driver.delete_all_cookies()
for cookie in cookieSli:
    #添加cookie
    driver.add_cookie(cookie)
driver.refresh()