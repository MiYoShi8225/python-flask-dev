"""
generatorの使いみちはメモリの削減をするために使う
"""
import sys
list_a = [i for i in range(10000)]

def num(max):
    i = 0
    while i < max:
        yield i
        i += 1

gen = num(10000)

#sys.getsizeof(変数名)　メモリー量を見る

print(sys.getsizeof(list_a)) #87616
print(sys.getsizeof(gen)) #112
