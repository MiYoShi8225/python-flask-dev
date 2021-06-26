# getter, setter

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        print('getter name を呼び出す')
        return self.__name

    def get_age(self):
        print('getter age を呼び出す')
        return self.__age
    
    def set_name(self, name):
        print('setter name を呼び出す')
        self.__name = name

    def set_age(self, age):
        print('setter name を呼び出す')
        self.__age = age

    name = property(get_name, set_name) #nameを指定するとget,setが呼び出される
    age = property(get_age, set_age)

    def print_msg(self):
        print(self.name, self.age)

human = Human('Taro', 15)
human.name = 'Jiro'
print(human.name)
print(human.age)
human.age = 19
print(human.age)

