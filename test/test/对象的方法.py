# info  = 'abcdea'
# for one in range(0,3):
#     print(one)
# idxList = []
# for one in range(0,len(info)):
#     if info[one] == 'a':
#         idxList.append(one)
# print(idxList)
#split 返回是列表,切点会被删除；
# info  = 'abcdeac'
# print(info.split('c'))
# lower 大写转化为小写
# upper 全部转化为大写
# replace 替换字符串里面的指定的子字符串('旧元素'，'新元素',1)1代表替换几个；
# info  = 'abcdeac'
# print(info.replace('c','x',1))
# strip将字符串前置空格和后置空格删除--->中间的元素不能去掉-->只能去头尾
# info  = '  abcde ac  '
# print(info.strip())

#扩展
info = '  abc  def  '

'''
去掉info中所有空格
方案一:
   1-info.strip()---去掉头尾的空格
   2-xx.spilt(' ')
   3-xx.join([xx,xx])
方案二
    info.replace(' ','')
    
'''
# a = [1,2,3,4,5,6]
# b = print(a[3])
# print(b[0])
