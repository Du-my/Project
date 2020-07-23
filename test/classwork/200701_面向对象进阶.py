#作者:老杜
#2020/7/3
#多继承
# class Class1:
#     def money(self):
#         print('有钱100万')
# class Class2:
#     def money2(self):
#         print('有钱200万')
# class Class3(Class1,Class2):
#     pass
# cls3=Class3()
# cls3.money()
# cls3.money2()

#多态
# class Fanguan:
#     pass
# class Yuxiangrousi(Fanguan):
#     def caidan(self):
#         print('鱼香肉丝')
# class Gongbaojiding(Fanguan):
#     def caidan(self):
#         print('宫保鸡丁')
# guke1 = Yuxiangrousi()
# guke2 = Gongbaojiding()
# guke1.caidan()
# guke2.caidan()

#递归
# def jiecheng(n):
#     if n==1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
# print(jiecheng(5))

#斐波那契前20位
list1 = []
for i in range(20):
    if len(list1)<2:
        list1.append(1)
    else:
        list1.append(list1[-2]+list1[-1])
print(list1)