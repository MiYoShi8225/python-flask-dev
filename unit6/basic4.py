#ポリモフィズム

from abc import abstractclassmethod, ABCMeta, abstractmethod

class Human(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name

    
    @abstractmethod #クラスごとに必ず再定義しなくては行けないものを決める
    def sya_something(self):
        pass

    def sya_name(self):
        print(self.name)

class Woman(Human):
    def sya_something(self):
        print('女性: 名前は{}'.format(self.name))


class Man(Human):
    def sya_something(self):
        print('男性: 名前は{}'.format(self.name))

num = input('0か1を入力してください')
if num == '0':
    human = Man('Taro')
elif num == '1':
    human = Woman('hanako') # @abstractmethodで定義した def sya_somethingを再定義しないとエラーになる
else:
    print('間違っています')

human.sya_something()



