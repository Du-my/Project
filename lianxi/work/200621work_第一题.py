
'''
请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。

请按下面算法的思路实现函数：

1. 创建一个新的列表newList
2. 先找出所有元素中最小的，append在newList里面
3. 再找出剩余的所有元素中最小的，append在newList里面
4. 依次类推，直到所有的元素都放到newList里面
'''

infoList = [1, 5, 8, 555, 33, 66, 87, 99, 56, 3, 0, -1, 999]
#定义一个函数 mySort
# def mySort(infoList):
#     newList = []
#     for one in sorted(infoList):
#         newList.append(one)
#     return newList
# print(mySort(infoList))   #调用方法打印排序后新列表从小到大排列
# print(infoList)    #sorted()方法不改变原列表数据

def mySort(inflList):
    newList = []
    while len(inflList) >0:  #循环条件判断列表如果长度>0进行循环
        minData =min(inflList)  #找到最小值
        newList.append(minData)  #把最小值新增到新列表
        inflList.remove(minData)  #删除最小值进行下一层循环
    return newList
print(mySort(infoList))