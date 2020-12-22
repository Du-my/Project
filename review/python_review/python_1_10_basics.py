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

