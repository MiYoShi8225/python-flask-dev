# プライベート変数

class Human:

    __class_val = 'Human'
    test = 'testmsg'

    def __init__(self, naem, age):
        self.name = naem
        self.age = age

    def print_msg():
        pass



human = Human('taro', 17)
print(human.name)

#print(human.__class_val)　←これはerrorになる
print(human._Human__class_val)
human.print_msg()
