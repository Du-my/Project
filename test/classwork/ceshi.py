#作者:老杜
#2020/7/6
import re
# a=["老王","老赵"]
# b=["老李","老刘"]
# # print(a+b)
# a.append(b)
# print(a)

# print(int("5.0"))
# for i in range(1,6):
#     if i%3 ==0:
#         break
#     else:
#         print(i,end=',')
# d={'abc':123,'def':456,'ghi':789}
# print(len(d))
# str1 = "Runoob example....wow!!!"
# str2 = "exam"
# print(str1.find(str2, 4))
str1='<html>a=”as1d32as1d654as54d65asd465asd4”</html>'

b=re.findall('<html>a="（.+？）”</html>',str1)
# <html>a=”（.+）”</html>
# <html>a=”（.*？）”</html>
# <html>a=”（.*）”
print(b)
a = re.findall('<html>a=”(.*)”',str1)
print(a)