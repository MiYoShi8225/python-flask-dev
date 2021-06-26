
# サブジェネレーター

def sub_sub_generator():
    yield "sub_sub_yield"
    return "sub_sub_return"

def sub_gererator():
    yield "sub_yield"
    res = yield from sub_sub_generator()
    print("su res = {}".format(res))
    return "sub_return"

def gererator():
    yield "gererator_yield"
    res = yield from sub_gererator()
    print('gen res = {}'.format(res))
    return "gererator_return"

gen = gererator()
print(1, next(gen))
print(2, next(gen))
print(3, next(gen))


print(4, next(gen))
print(5, next(gen))

