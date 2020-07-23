#作者:老杜
#2020/7/3
from random import randint
import time
class Tiger:#创建老虎类
    def __init__(self):
        self.name = '老虎'
        self.weight = 200
    def roar(self):
        print('小老虎Wow~叫了一声，体重减5')
        self.weight-=5
    def eat(self,food):#投食函数判断喂的什么
        if food =='meat':
            self.weight+=10
            print('喂的是肉，体重+10')
        elif food=='grass':
            self.weight-=10
            print('喂的是草，体重-10')
class Sheep:#创建山羊类
    def __init__(self):
        self.name = '羊'
        self.weight = 100
    def roar(self):
        print('哦吼~小羊咩~叫了一声，体重减5')
        self.weight-=5
    def eat(self,food):#判断羊的投喂
        if food =='grass':
            self.weight+=10
            print('喂的是草，体重+10')
        elif food=='meat':
            self.weight-=10
            print('喂的是肉，体重-10')
class Rooms:#房间类
    def __init__(self,roomno,kind):#房间号，种类
        self.roomeno = roomno
        self.kind = kind
def chushihua():#对房间进行初始化，生成10个房间
    roomList=[]
    for i in range(1,11):
        if randint(0,1)==0:#随机进入一个房间不是老虎就是山羊，进入后实例化
            kind = Tiger()
        else:
            kind = Sheep()
        room=Rooms(i,kind)#实例化房间类将动物循环放入房间
        roomList.append(room)
    return roomList
def playGame():#玩游戏
    fangjian =chushihua()#先初始化创建房间
    endTime = time.time()+180#三分钟
    while endTime-time.time()>0:#结束时间大于0继续循环
        rand=randint(0,9)
        fang=fangjian[rand]
        panDuan1= input(f'现在开始访问{rand+1}号房间，请问需要敲门吗？[y/n]')
        if panDuan1=='y':
            fang.kind.roar()
        panDuan2= input('请问是否需要喂食？[y/n]')
        if panDuan2=='y':
            food = input('请输入要喂食的食物[meat/grass]')
            fang.kind.eat(food)
    else:
        print('游戏结束了，别玩了，自己再写一个')
        j=1
        for i in fangjian:
            print(f'房间号{j},动物是{i.kind.name},体重是{i.kind.weight}')
            j+=1
#当前文件调用
if __name__=='__main__':
    playGame()
