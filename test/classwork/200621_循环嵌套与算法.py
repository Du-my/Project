#循环嵌套与算法
# list1 = ['张三','李四','王五']
# list2 = ['苹果','香蕉','西瓜']
# for i in range(0,3):
#     for j in range(0,3):
#         print(list1[i]+'吃' +list2[j])

#普通方式实现需求

# beforetax =[10000,15000,8000,4000,5000]
# aftertax = []
# for one in beforetax:
#     aftertax.append(one *0.9)
# print(aftertax)

# #列表生成式实现这个需求
# #优点：代码简短，缺点：代码可读性略差
# aftersal =[i*0.9 for i in beforetax]
# print(aftersal)

# a = list(range(1,11))
# print(a)
#100以内的所有奇数,不是奇数的位置写偶数

# a = [i if i%2==1 else '偶数'for i in range(1,100)]
# print(a)
# #输出奇数1-100
# b = [i for i in range(1,100) if i%2==1]
# print(b)

#python可以自带排序方法
list1 = [3,66,77,0,-1,5,18]
# list1.sort()#sort()自带排序，对列表永久排序
# print(list1)
# print(sorted(list1))#sorted()临时排序，不会影响到原列表
# list1.reverse()#翻转
# list1[::-1]#以切片进行翻转
# #倒序
# # list1 = [3,66,77,0,-1,5,18]
# # list1.sort(reverse=True)#sort()自带排序，对列表永久排序
# # print(list1)
#冒泡排序
#两两之间进行比较

for i in range(len(list1)-1):
    for j in range(len(list1)-1-i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
        else:
            pass
print(list1)

