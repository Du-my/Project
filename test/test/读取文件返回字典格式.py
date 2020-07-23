'''
1.读取文件每一行数据；
2.提取每一行中有效数据；
3.统计输出
('2017-03-13 11:50:09', 271, 131),
step over 单独运行--每一行就是一步
'''
fileDir = 'D:/github\wendang/0005_1.txt'
def putInfoToDict(fileName):
    #1.打开文件
    resDict = {}
    with open(fileName) as fo:
        #2.读取所有行数据
        lines = fo.read().splitlines()#列表
        # print(lines)
        #3.对每一行数据进行遍历
        for line in lines:
            line = line.replace('(','').replace(')','').replace("'",'').replace(';',',')
            temp = line.split(',')
            checkTime = temp[0].strip()
            lessonId = int(temp[1].strip())
            userId = int(temp[2].strip())
            info =  {'lessonid': lessonId,'checkintime':checkTime}
            #4.统计
            if userId not in resDict:#新增键值对存储
                resDict[userId]=[info]
            else:#存在--append--列表中
                resDict[userId].append(info)
    return  resDict

res = putInfoToDict(fileDir)
print(res)
#完美打印
import pprint

pprint.pprint(res)