# 特殊メソッド

class Human:
    def __init__(self, name, age, phone_num):
        self.name = name
        self.age = age
        self.phone_num = phone_num

    def __str__(self):
        return 'human'

    def __eq__(self, other):
        return (self.name == other.name) and (self.phone_num == other.phone_num)

    def __hash__(self):
        return hash(self.name + self.phone_num)
    
    def __bool__(self):
        return True if self.age >= 20 else False
    
    def __len__(self):
        return len(self.name)

man = Human('Jiro', 18, '0801111111')
man2 = Human('Jiro', 22, '0801111111')
man3 = Human('Taro!', 22, '0901111111')
print(man) #オブジェクト情報ではなくて、strのリターンで返される'human'が返される

print(man == man2) #eqの情報を参照して←の式のbooleanを返す。

# print(hash('Taro'))
# print(hash('Taro'))
# print(hash('Jiro'))

set_men = {man, man2, man3}
for x in set_men:
    print(x)

print(len(man))
print(len(man3))
