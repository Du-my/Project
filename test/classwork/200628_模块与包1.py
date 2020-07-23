#模块与包1
# def fun1(a,b):
#     return a+b
# import time#加载一个模块的语句
# time.sleep(0.1)

# import __hello__
# import this #pythom 之禅
#模块的概念。其实 就是一盒.py文件
#包的概念：存放若干个模块的文件夹；有__init__文件；
# def sumdata(a,b):
#     return a+b


# import sumdata1
# print(sumdata1.sumdata(3,6))#模块名.函数名

# from 模块名 import  函数名
from sumdata1 import sumdata
print(sumdata(3,6))

# import (包名.模块名)
# from 包名 import 模块名
#from 包名.模块名 import 函数名



