#再识函数
#函数的作用域
# a=0
# e = 76
# def fun1(c,d):
#     global e #声明e为全局变量
#     e=3 #e为局部变量
#     return (c+d)*e
# print(fun1(3,6))
# print(a)
#set缺省值默认空格，可以自己重新复制
# print('a','b','c',sep='我的乖乖')
# print('a','b','c',end='结束符')#a b c结束符

# import time
# print('==========Loading==========')
# for i in range(0,101):
#     print('\r',f'当前进度{i}%',end='',flush=True)
#     time.sleep(0.1)

# import time
# print('上课倒计时')
# for i in range(10,-1,-1):
#     print('\r',f'上课开始倒计时{i}秒',end='',flush=True)
#     time.sleep(1)
#     if i==0:
#         print('上课啦')
#
#*args可变数量参数，或叫位置参数，允许在传递实参时，传递不定数量的参数
# def func(a,b,*args):
#     print(a,b,args)
# func(1,2,3,45455,666,77,787)

#关键字参数**kwargs   位置参数永远在关键参数的前面
def func(a,b,*args,**kwargs):
    print(a,b,args,kwargs)
func(1,2,3,4,5,6,6,7,8,qqq='32')


