#作者:老杜
#2020/7/4
# 动物园里面有10个房间，房间号从1 到 10。
#
# 每个房间里面可能是体重200斤的老虎或者体重100斤的羊。
# 游戏开始后，系统随机在10个房间中放入老虎或者羊。
#
# 然后随机给出房间号，要求游戏者选择敲门还是喂食。
#
# 如果选择喂食：
# 喂老虎应该输入单词 meat，喂羊应该输入单词 grass
# 喂对了，体重加10斤。 喂错了，体重减少10斤
#
# 如果选择敲门：
# 敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。
#
#
# 游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。
# 游戏3分钟结束后，显示每个房间的动物和它们的体重。

# 想象一个老虎的类，老虎会叫（叫一次体重减5），
# 老虎也可以吃肉，（如果吃对了，体重会增加10，如果吃错了，体重会减少10）
# 老虎的基本属性，老虎的名字是'老虎'，老虎的体重是200.
from random import randint
import time


class Tiger:
    def __init__(self):
        self.name = '老虎'  # 在此题中，所有的实例都是一样的，名字为老虎，体重为200，所以直接写在了初始化方法中
        self.weight = 200

    def roar(self):
        print('Wow~~，体重减5')
        self.weight -= 5

    def eat(self, food):
        if food == 'meat':
            self.weight += 10
            print('喂食正确，体重增加10！')
        elif food == 'grass':
            self.weight -= 10
            print('喂食错误，体重减少10！')


class Sheep:
    def __init__(self):
        self.name = '羊'
        self.weight = 100

    def roar(self):
        print('咩~~，体重减5')
        self.weight -= 5

    def eat(self, food):
        if food == 'grass':
            self.weight += 10
            print('喂食正确，体重增加10！')
        elif food == 'meat':
            self.weight -= 10
            print('喂食错误，体重减少10！')


class Rooms:
    def __init__(self, roomno, kind):  # 房间的类，里面有房间号和动物类别两个实例属性
        self.roomno = roomno
        self.kind = kind


def chushihua():  # 对房间进行初始化，生成10个房间，每个房间里是随机的老虎或羊
    roomlist = []
    for i in range(1, 11):
        if randint(0, 1) == 0:
            kind = Tiger()  # 实例化一个老虎
        else:
            kind = Sheep()  # 实例化一个羊
        room = Rooms(i, kind)  # 循环放10个动物到房间里
        roomlist.append(room)
    return roomlist  # 将这10个房间作为返回值


def game():
    fangjian = chushihua()  # 获取到初始化之后的10个房间的列表
    endtime = time.time() + 10  # 确定一个结束时间
    while endtime - time.time() > 0:  # 如果结束时间大于当前时间，就执行循环
        rand = randint(0, 9)  # 随机生成一个0-9之间的数字
        fang = fangjian[rand]  # 将刚才生成的数字作为房间列表的下标，随机给一个房间
        panduan1 = input(f'现在开始访问{rand + 1}号房间，请问需要敲门吗？[y/n]')
        if panduan1 == 'y':
            fang.kind.roar()  # 调用动物的叫的方法
        panduan2 = input('请问是否需要喂食？[y/n]')
        if panduan2 == 'y':
            food = input('请输入要喂食的食物[meat/grass]')
            fang.kind.eat(food)  # 调用动物的吃的方法
    else:
        print('游戏结束')
        j=1
        for i in fangjian:
            print(f'房间号{j},动物是{i.kind.name},体重是{i.kind.weight}')
            j+=1
        # for j, i in enumerate(fangjian):
        #     print(f'房间号{j},动物是{i.kind.name},体重是{i.kind.weight}')


if __name__ == '__main__':
    game()