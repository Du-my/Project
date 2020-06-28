
#读取文件的地址
fileDir = 'D:/github\wendang/0005_1.txt'

def putInfoToDict(fileName):
    #读取文件
    # 定义一个字典存储数据
    infoDict = {}
    with open(fileName) as ifile:
        #读取文件中每一行的数据
        lines = ifile.read().splitlines()
        # print(lines)
        #循环遍历接收到的每行数据
        for line in lines:
            #替换遍历的列表中数据多余字符
            line = line.replace('(','').replace(')','').replace("'",'').replace(';',',')
            #以,号截取列表数据
            temp = line.split(',')
            #列表中数据对应值并且去掉前后空格
            checkintime = temp[0].strip()
            # print(checkintime)
            lessonId = int(temp[1].strip())
            # print(lessonId)
            userId = int(temp[2].strip())
            # print(userId)
            #封装一个字典存储数据
            info = {'lessonid': lessonId,'checkintime':checkintime}
            #判断用户是否在字典中
            if userId not in infoDict:#不在字典中时新增一个键值对
                infoDict[userId] = [info]
            else:#存在时添加到列表里面
                infoDict[userId].append(info)
    return infoDict

res = putInfoToDict(fileDir)
print(res)
#导入打印
import pprint
pprint.pprint(res)
'''
疑问:为什么使用pprint后输出的字典数据没有按照输入时的顺序排序，自己没有找到解决办法希望老师讲解作业时帮忙解答一下
'''