#作者:老杜
#2020/7/5

import re#加载正则表达式
# str1='songqin'
# a=re.findall('s.',str1)#dindall的返回值是一个列表
# print(a)
#  *号标识0到n位字符
# a = re.findall('s.*',str1)#匹配s后的所有值
# print(a)
# b = re.findall('s.*g',str1)#匹配s后到g的所有值，包含s和g
# print(b)
#.*?做偷懒匹配
# a = re.findall('s.*?',str1)#匹配s后的任意字符，就不在匹配了；
# print(a)
# b = re.findall('s.*?g',str1)#匹配s后到g的所有值，包含s和g，匹配到就停
# print(b)
#（.*?）带上括号后，就不包含边界值
# a = re.findall('so(.*?)in',str1)
# print(a)
#（.*?）带上括号后，就不包含边界值
# a = re.findall('so.+?',str1)
# b = re.findall('so.*?',str1)
# print(a)
# print(b)

#   \w表示匹配字母数字下划线
# str2 = 'abc$de'
# a=re.findall('\w{3}',str2)
# print()
# #    \表示匹配非字母数字下划线
# b=re.findall('\W',str2)
# print(b)
# # \s  空字符串，以及\t制表符，换行符\n
# str7 ='   abc  \n  '
# c=re.findall('\s',str7)
# print(c)
# d=re.findall('\S',str7)
# print(d)
# #   \d匹配数字  \D匹配非数字
# str8 ='sjvhv1739bhbjb7df7'
# e=re.findall('\d',str8)
# print(e)
# f=re.findall('\D',str8)
# print(f)
# #修饰符re.I不区分大小写
# str3= 'abcABCaBCDFt'
# a1=re.findall('abc',str3)
# a2=re.findall('abc',str3,re.I)
# print(a1)
# print(a2)
# #修饰符re.S匹配所有字符
# str4= 'abcABCa\nBCD\tFt'
# a3=re.findall('.*',str4)
# a4=re.findall('.*',str4,re.S)
# print(a3)
# print(a4)
# ^匹配开头 $匹配结尾
list1=['abc','deabc','ffabcfff']
for i in list1:
    print(re.findall('abc$',i))
