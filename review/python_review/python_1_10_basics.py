import  math
print(math.pi)

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

#条件判断







