# #  求1+.。。。。100的值；
#
def get_sum(start,end,step=1):#函数说明
    '''

    :param start: xxxx
    :param end: xxxx
    :param step: xxxx
    :return:
    '''
    sumData = 0#结果和
    i =start #起始值
    while i<=end:
        sumData+=i
        i+=step
    return sumData
res = get_sum(1,10)
print(res)
print(get_sum.__doc__)#打印函数说明

# nameList = ['tom','lili','jack']
# i = 0
# while i<len(nameList):
#     print(nameList[i])
#     i+=1
#
# #  for 循环
# for name in nameList:
#     print(name)
'''
1.while 靠条件结束的循环，不知道循环次数；
2.for  遍历操作，如果for后面为空，那么这个for不会进入里面运行
'''
#for 需要描述循环次数--range
# for one in range(5,0,-2):
#     print(one)
'''
jmeter做并发需要对账号密码进行参数化---需要一个数据文件
需要1000条数据；
'''
# for one in range(1,1001):
#     info = f'sq{one:0>3},123456'
#     print(info)

#break---中断
# for one in range(0,5):
#     if one==2:
#         # break  #结束本层循环
#         continue  #结束本次循环，继续下次；
#     print(one)
nameList = ['tom','lili','jack']
for one in range(0,2):
    for name in nameList:
      if name=='lili':
        break  #结束本层循环
      print(name)