#文件的读取及写入
#open（） 打开文件 w表示写入 r代表读取 追加读取

#\n有特殊含义类似的还有\t在\前面再加一个\,表示\不转义；
#也可以在字符串外面加一个r，表示后面的字符串不转义；
# flie1 = open('D:\github\wendang\\note1.txt')
# flie1 = open(r'D:\github\wendang\note1.txt')
# flie1 = open('D:/github\wendang\note1.txt')
#当r模式时，如果找不到文件，会报错
# print('文件指针的位置：' +str(flie1.tell()))#返回目前指针当前所在位置
# print(flie1.read(3))
# print('文件指针的位置：' +str(flie1.tell()))
# flie1.read(10)
# flie1.seek(10)#参数1：光标偏移多少位，参数2：可以不用写默认为0，表示从文件头开始计算
#如果seek（）的第二个为1或者2，1表示从指针的当前位置开始偏移，2表示从文件末尾开始偏移
#seek()的第二个参数如果是1和2，那么只有rb模式才能用，rb是以二进制方式读取文件
# print(flie1.read())

# print(flie1.readline())#读取文件的一行
# print(flie1.readline())#读取文件的一行

# print(flie1.readlines()[0])#读取文件的多行，返回值是列表形式
# flie1.seek(0)#回到文件开始位置
# print(flie1.readlines()[1])
#\n \t表示rb模式中表示换行
# print('文件指针的位置：' +str(flie1.tell()))
# print(flie1.read())
# print(flie1.read().splitlines())#去掉换行符，返回值是列表类型
#
#
# flie1.close()#关闭文件  在open（）函数的最后，要使用close（）方法
#

#文件的写入
# w方法表示写入，并且会清楚文件之前的内容；
# flie1 = open('D:/github\wendang/note1.txt','w')
# flie1.write('莫听穿林打叶生\n何妨吟啸且徐行')
# flie1.close()
#a也代表写入，会接着文件后面继续写
# flie1 = open('D:/github\wendang/note1.txt','a')
# #没有文件时a模式和w模式会自动添加文件  r模式找不到文件会报错
# flie1.write(',月高高的挂无垠')
# flie1.close()

#同时进行读取和写入的模式  r+可同时进行读写，之前的内容会覆盖
# w+可同时读写清楚以前的内容 a+可同时读写，从文件末尾接着写
# flie1 = open('D:/github\wendang/note1.txt','w')
# flie1.write('莫听穿林打叶生\n何妨吟啸且徐行')
# flie1.close()

#with open() #是open（）的升级版，不需要写close（）方法
flie1 = open('D:/github\wendang/note1.txt','a+')

with open('D:/github\wendang/note1.txt','a+') as flie1:
    flie1.write('\n两行放一起')



