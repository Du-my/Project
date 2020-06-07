'''
函数：
   1.在一个xxx.py文件中
   2.函数的调用  test()
对象的方法：
    1.本质也是一个函数，这个函数不在xxx.py里，在class类里面

'''
# def test(a,b):
#  print(a + b )
# test(1,2)

# #方法调用
# ''.strip()

#字符串的方法
#count 计算字符串中包含多少个指定的子字符串
info = 'abcdea'
# print(info.count('a'))
# if info.count('x')!=0:      #检查点--->断言
#     print('x  在这个字符串里面')
# else:
#     print('x  不在这个字符串里面')

#    endswith  检查字符串是否以指定的字符串结尾  ----bool类型
# print(info.endswith('a'))

#   find 返回指定的子字符串（一个元素或多个连续元素）在字符串中出现的位置
#1.不清楚结果  2.能找到，找不到。。
#  返回第一个找到刚元素出现的下标
print(info.find('x')) 
if info.find('a')!=-1:
    print('刚元素存在')#可以设置检查点
else:
    print('不存在该元素')
#  index ---求元素下标，这个元素一定要存在，否则报错
print(info.index('a'))
print(info.index('b'))
print(info.index('c'))
print(info.index('e'))
print(info.index('f'))
print(info.index('f'))
print(info.index('f'))
print(info.index('f'))
print(info.index('f'))
print(info.index('f'))