"""
*arg1 可変長のタプル
**arg2 可変長の辞書
"""

def sample(arg1 ,arg2 = 100):
    print(arg1, arg2)

sample(200)

sample(300, 200)

def spam(arg1, *arg2):
    print("arg1 = {}, arg2 = {}".format(arg1, arg2))

spam(1,2,3,4,5)

def spam(arg1, **arg2):
    print("arg1 = {}, arg2 = {}".format(arg1, arg2))

spam(1, name='taro',age=17)


def sample_2():
    return 1,2

a,b = sample_2()
print(a, b)


