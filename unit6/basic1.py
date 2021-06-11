# クラスの継承

class Person: #親クラス
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print('hello {}'.format(self.name))
    
    def sya_age(self):
        print('age is {}'.format(self.age))

class Employee(Person): #Personの機能を継承する

    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number =number

    def say_number(self):
        print('my number is {}'.format(self.number))
    
    def greeting(self): #オーバーライド(上書きする)
        super().greeting()
        print('I \'m employee phone number = {}'.format(self.number))
    
    # def greeting(self, age): #オーバーロード() Pythonじゃ出来ない！
    #     print('オーバーロード')

man = Employee('Tonegawa', 40, '08000000000')
man.greeting()
man.say_number()
man.sya_age()