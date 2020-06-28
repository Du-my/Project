#格式化字符串
# info = '我叫%s，你叫%s,他叫%s，年龄是%s' %('张三','李四','王五',22) #格式化字符串最后，是元组形式
# print(info)

# info = '我叫%s，你叫%s,他叫%s，年龄是%-5s' %('张三','李四','王五',223434) #格式化字符串最后，是元组形式
# print(info)


# print('%05d'%99)
# print('%5d'%99)

print('%9.3f'%3.1415926)

# 接口自动化--request body
# temNum = '13522933931'
# adduser_data ='''{
# "aac003": "tom",
# "tel": "%s",
# "aac011": "21",
# "aac030": "12345",
# }''' % temNum
# print(adduser_data)

inputStr = input('Please input student age info:')
studentInfo = inputStr.split(';')
for one in studentInfo:
    # check if it is valid input
    if ',' not in one:
        continue

    name, age = one.split(',')
    name = name.strip()
    age = age.strip()

    #  check is age digit
    if not age.isdigit():
        continue

    age = int(age)

    print('%-20s :  %02d' % (name, age))
    # print('{:20} :  {:02}'.format(name, age))
    # print(f'{name:20} :  {age:02}')
