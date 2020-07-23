#作者:老杜
#2020/7/3
# try:
#     a = 0
#     print(100/a)
# except ZeroDivisionError:
#     print('0不能做为分母')
# try:
#     a = 0
#     print(100 / a)
# except Exception as e:
#     print(e)
# try:
#     list1=[1]
#     print(list1[1])
# except IndexError as e:
#     print(e)
# try:
#     a = 0
#     print(100 / a)
# except Exception as e:
#     print(e)
# else:
#     print('程序没有出现问题')
# finally:
#     print('不管有没有异常都显示')

#将程序异常写日到日志：
# import traceback
# import time
# import logging
# try:
#     a = 0
#     print(100 / a)
# except Exception as e:
#     logging.basicConfig(filename='D:/logging.log',filemode='a+')
#     logging.error(time.strftime('%y-%m-%d %H:%M:%S'))#向日志中写入时间戳
#     logging.error(traceback.format_exc())#将具体的报错信息写入到日志中