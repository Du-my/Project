'''
1.程序开始的时候提示用户输入学生年龄信息 格式如下：

Jack Green ,   21  ;  Mike Mos, 9;

我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格）

2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green :   21;
Mike Mos   :   09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
'''

#输入学生姓名及年龄
inputstr = input('请输入学生姓名及年龄（多条数据以;间隔）:')
#以分号截取字符串信息
student =inputstr.split(';')
#循环遍历截取字符串数据
for one in student:
    #判断遍历的数据没有’,‘时跳过继续执行
    if ',' not in one:
        continue
    #定义两个变量接收以’,‘截取的遍历数据
    name = one.split(',')
    age = one.split(',')
    #去掉前后空格
    name = name[0].strip()
    age = age[1].strip()
    #判断年龄字符串中信息不是纯数字时跳过当前循环继续执行
    if not age.isdigit():
        print('您输入的学生年龄中含有非数字字符，请重新输入')
        continue
    age = int(age)#年龄转化为int类型
    print(f'{name:<20}:{age:0>2}')
'''
       11题总结:
    1-调用isdigit()方法时age.isdigit后面没加括号导致运行时报错
    2-代码逻辑思维能力不灵活，需要多练多敲

'''
