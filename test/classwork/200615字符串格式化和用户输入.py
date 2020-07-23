print('字符串格式化输出')
'''
字符串的格式化；
概念：表达描述一个字符串---就是一个字符串
使用场景： 往字符串里面传入对应的值：
   方案一：
   方案二：

'''
#字符串描述
# name = 'tom'
# age = 20
# info = '我叫：' +name +' 年龄：' +str(age)
# print(info)
#方案一%s 字符串转换  %d 有符号的十进制数    %f转成浮点数  %x 转成无符号得十六制数；
# name = 'tom'
# age = 20
# info = '我叫： %s,年龄是：%s' %(name,age)
# print(info)
# print('%5d' % 56)#正数---右对齐--左补齐，补空格
# print('%-5d'  % 56)
# #如果要求宽度<数据本身宽度---这个要求不理会；
# print('%6.2f' % 3.1415926)
# #实际应用

#接口自动化--request body
# temNum = '13522933931'
# adduser_data ='''{
# "aac003": "tom",
# "tel": "%s",
# "aac011": "21",
# "aac030": "12345",
# }''' % temNum
# print(adduser_data)

#方案二
#1-顺序传值法 format(xx,xx),按照顺序传入需要传入的参数，位置不能为空，否则下标越界；
#< 左对齐右补齐    >右对齐左补齐   ^中间对齐
name = 'tom'
age = 20
info = '我叫:{:0^6},\n年龄是:{:*^6}'.format(name,age)
print(info)
#2-下标传值法
info = '我叫:{0:>6},\n年龄是:{1:>6}'.format(name,age)
print(info)
#3-变量传值法 ---一般不使用
info = '我叫:{name:>6},\n年龄是:{age:>6}'.format(name='tom',age='36')
print(info)
#pythom3.6后
info = f'我叫:{name:>6},\n年龄是:{age:>6}'
print(info)