# setter, getter その2

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self): #getter
        print('getter nameが呼ばれました')
        return self.__name
    
    @property
    def age(self):
        print('getter ageを呼び出しました')
        return self.__age
    
    @name.setter
    def name(self, name):
        print('setter nameが呼ばれました')
        self.__name = name

    @age.setter
    def age(self, age):
        print('setter ageを呼び出しました')
        if age >= 0:
            self.__age = age


human = Human('taro', 13)
print(human.name)
human.name = 'Makoto'
print(human.name)
