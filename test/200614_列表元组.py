# list = [1,2,3,4,5,6,'str1','str2']
# print(list)
# list[0] = '修改'
# print(list)
# print(list[:6:2])
# print(list[-1][0:2])
#
# #在字符串尾部添加
# list.append(988)
# print(list)
# #在指定下标位置添加
# list.insert(1,150)
# print(list)
# #列表的拼接
# list.extend([666])
# print(list)
# #删除列表中的元素1,默认删除最后一位，可以根据下标删除指定元素
# list.pop(2)
# c=list.pop(2)
# print(list)
# print('被删除的值是' + str(c))
# #删除列表中的元素2,删除指定的值，需要参数
# list.remove(6)
# print(list)
# #删除列表中的元素3,根据下标删除指定的值
# del list[0]
# print(list)

#元组，元组中的值无法修改

list = [1,2,3,4,5,6,'str1','str2',[12,22]]
print(list)
print(list[-2:])
print(list)
a = 'my name is XXX '
b =a [-5:]
print(b)

list[-1][1]=66
print(list)
a = "'what's your name'"
print(a)
a = (3,4)
print(a)

