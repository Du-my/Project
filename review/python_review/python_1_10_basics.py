# import  math
# print(math.pi)
'''
#字符串
print('He said: "Nice to see you!"')
#切片
a = 'ABCDEFG'
print(a[2:5])

a='gsdfjfsgdfjsdgfisdgflsdhgfsldgflsdgflsidgfisodygfiosdyugfoisdgfsdhfvsduhyfvgsduhyvfsudyfusydvfuysdgvfuysdgfusydvfusdygfusydgfsd'

print(len(a))
print(a[0:150])
#列表与元组
list1 = [1,2,3,4,6,[8],[12,13,14]]
list1.append(100)  #自动添加到末尾
list1.insert(1,999)  #插队到指定位置
print(list1)
list1.pop()#删除列表的最后一个元素，也可以输入要删除的下标，可以接受到删除的值
print(list1)
list1.remove(2)#删除指定参数的值，多个值时只删一个，删第一个
print(list1)
del list1[0]#删除对应下标数据
print(list1)

#布尔表达式
#True表示真，False表示假，True代表1，False代表2
from selenium import webdriver
a = webdriver.Chrome()
a.get("https://www.baidu.com")
b = a.find_element_by_id('kw')
print(b.is_displayed())
'''
#条件判断

#深拷贝和浅拷贝
'''
list3 = [11,[22,33],44,55]
list4 = list3[:]   #切片就是一种浅拷贝
print('原列表'+str(list3))
list3.append(77)
print('变更后的list3'+str(list3))
print('没有变更的list4'+str(list4))

import  copy
list4= copy.copy(list3)#浅拷贝
list4 = copy.deepcopy(list3)#深拷贝
'''
#条件判断
'''
# a = 1
# if a>9:
#     print('不错')
# else:
#     print('好吧')

a = int(input('请输入一个数字:'))
if a>=90:
    pass
elif a>=80:
    print('还行')
elif a>=70:
    print('不错')
else:
    print('最后')
'''

#初识函数
'''
def sumdata(a,b):
    print(a+b)
    return a+b
sumdata(100,200)
print(sumdata(100,200)**2)

a = "临兵斗者皆阵列前行"
print(list(a))
'''
#对象的方法
'''
#strip()去掉前后空格
print('****************12月22日*******'.strip('*'))
#count()统计某个字符出现在字符串的数量
print('****************12月22日*******'.count('*'))
'''

#字符串的格式化和用户输入
'''
info = '我叫%-5s，年龄是%5d'%('张三',24)
print(info)

print('%f'%3.1415926)
print('%.3f'%3.1415926)

print('my name is {:6},I am {:06} years old'.format('杜梦豪',25))
print('my name is {:>6},I am {:6} years old'.format('杜梦豪',25))
print('my name is {:<6},I am {:06} years old'.format('杜梦豪',25))
print('my name is {:^6},I am {:06} years old'.format('杜梦豪',25))

print('my name is {1},I am {0} years old'.format('杜梦豪',25))

name='杜梦豪'
age = 25
info1=f'我叫{name},年龄{age}'
print(info1)
'''
#循环语句与注释
'''
# i=1
# sumdata = 0
# while i<=10:
#     print(i)
#     i = i+1
#
# while i<=100:
#     sumdata = sumdata+i
#     i = i+1
# print(sumdata)

# for i in range(1,101):
#     sumdata=sumdata+i
# print(sumdata)

# list1 = ['张飞','关羽','刘备','赵云','黄忠']
# for i in list1:
#     print(i)

# def get_sum(start,end,slep):
#     sumdata = 0
#     i=start
#     while i<=end:
#         sumdata = sumdata+i
#         i=i+slep
#     return sumdata
# print(get_sum(1,100,2))
'''
#文件的读取与写入

file1= open('d:/note1.txt','r+')
# print(str(file1.tell()))#返回当前指针所在位置
# print(file1.read())
# file1.seek(3)#光标偏移多少位，第二个参数默认为0，1表示从开头，2从末尾，12只有rb模式才能用
# print(str(file1.tell()))#返回当前指针所在位置
# file1.seek(0)
# # print(file1.readlines())
# print(file1.readline())
file1.write('我这一生漂泊四海看淡今朝')
file1.write('莫听穿林打叶生')
print(file1.read())
file1.close()










