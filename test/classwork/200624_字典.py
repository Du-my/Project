#字典：一种存储数据的数据类型，它是通过键值对来存储数据  dict
#键值对成对出现
#字典本身是无序的，它不关注顺序
#值可以存放任何类型的数据--数字，字符串，元组，列表，字典， 键可以放字符串，数字，元组，不能是列表，字典
#在字典中键是唯一的



# dict1 ={'A':'Apple','B':'Book','C':'Cake','D':'Duck','E':'Easy'}
#
# nameList = [['Mick',25,180,80],['QQ',28,169,65],['Tom',26,178,82]]
# print(nameList[1][0])

# nameList2 = {'name':'Mike','age':'25','height':'169','weight':'65',
#              'name2':'Tom','age2':'26','height2':'175','weight2':'78'}
# print(nameList2)

# dict2  ={'abc':'123'}
# print(dict2)

#新增字体中元素
# dict3 = {'AA':'A1'}
# # print(dict3)
# dict3['AB']='A2'
# print(dict3)
# dict3['AB']='B2'
# print(dict3)
#
# #updata方法可以新增或者修改多个
# dict3.update({'姓名':'杜梦豪','年龄':'33'})
# print(dict3)

#清空字典
# dict3={}#内存中的地址重新生成了
# dict3.clear()#内存中的地址不变
# print(dict3)

#判断某个值在字典中，根据键判断，并且区分大小写
# if 'AC' in dict3:
#     print('在字典里')
# else:
#     print('不在字典')

#获取到字典中所有的键，所有的值，以及同时获取键和值
#key()方法的返回值属于类列表
# print(dict3.keys())
# #可以使用list()方法转化为真正的列表
# print(list(dict3.keys())[0])
#
# #获取到字典中所有的值,返回值也是类列表
# print(dict3.values())
#
# #同时获取键和值
# print(dict3.items())
#
# for key,value in dict3.items():
#     print((f'键:{key},值:{value}'))
vipData = '''{
    "aac003":"Tom",
    "tel":"13522933931"
}'''
import json
#json文件转换前为str类型
#将json转换为字典格式
# temp = json.loads(vipData)
# print(temp)

#将字典转为json格式
# print(json.dumps(temp))

#从文件中读取文件
with open('D:/github\wendang/note2.txt') as ofile:
    # a=ofile.read()
    # print(a)
    temp= json.load(ofile)
print(type(temp))

# with open ('D:/github\wendang/note2.txt') as ofile:
#     temp=json.load(ofile)
# print(temp)

# with open('D:/github\wendang/note2.txt') as ofile:
#     temp=json.load(ofile)
# print(temp)

