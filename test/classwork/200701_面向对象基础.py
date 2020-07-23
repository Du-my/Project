#作者:老杜
#2020/7/2
class Changfangxing:
    def __init__(self,chang,kuan):#初始化方法
        self.chang  = chang
        self.kuan  = kuan
    def zhouchang(self): #实例的方法，只能实例来调用
        return (self.chang+self.kuan)*2

    def mianji(self):
        return self.chang * self.kuan
    #类方法   =====可以由类本身来调用，也可以由实例调用
    @classmethod
    def tezheng(cls):
        print('两边得长相等，两边得宽也相等')
    #静态方法-------可以由类调用，也可以实例调用，本身是一个函数，只是放在了类下面
    @staticmethod
    def fun1(a,b):
        print(a+b)

cfx = Changfangxing(6,4)
print(cfx.zhouchang())
print(cfx.mianji())
print(cfx.__dict__)
Changfangxing.tezheng()
Changfangxing.fun1(3,5)
#加载inspect模块，这是一个python的自检模块，判断是否是某一种对象
import inspect
inspect.ismethod(Changfangxing.tezheng())

class Zhengfangxing(Changfangxing):
    def __init__(self,bianchang):
        self.chang=bianchang
        self.kuan=bianchang
zfx = Zhengfangxing(6)
print(zfx.zhouchang())
print(zfx.mianji())
