# ジェネレーター関数

def generator(max):
    try:
        print('ジェネレータ作成')
        for n in range(max):
            x = yield n
            print('x :{}'.format(x))
            print('yield実行')
    except ValueError as e:
        print('stopさせたよ')

# gen = generator(10)

# print(gen)

# n = next(gen) #1回目

# print(gen)
# print(n)

# n = next(gen) #2回目

# print(gen)
# print(n)

'''
nextで呼び出されたらyieldまでを実行するのがジェネレータ関数
'''

# for x in gen:
#     print('x :{}'.format(x))
    

gen = generator(10)

print(next(gen))
gen.send(100)
#gen.throw(ValueError('invalid Error'))　#ジェネレーター関数に無理やりエラーを発生させる
gen.close() #ジェネレータ関数の処理を終了する
next(gen)
