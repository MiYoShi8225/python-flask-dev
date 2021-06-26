# 文字列型

fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10)

fruit_10 = fruit * 10

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
banana
greap
"""
print(fruits)

fruit = 'banana'
print(fruit[1]) #bananaの2番目のaが表示

# count
msg = 'ABCDABC'
print(msg.count('A'))

# startswith, endswith
print(msg.startswith('ABCD')) #はじめの文字が正しかったらtrue 間違ってたらFalse

msg = '  ABCDEFABC'
#strip(両端) rstrip(右端) lstrip(左端)
print(msg.strip())

msg = 'ABCDEFABC'
print(msg.lstrip('CBA'))
print(msg.rstrip('CBA'))

# upper , lower, swapcase ,replace, capitaize
msg = 'abcABC'
msg_u = msg.upper() #大文字
msg_l = msg.lower() #小文字
msg_s = msg.swapcase() #小文字大文字の入れから
print(msg_u, msg_l, msg_s)


msg = 'ABDDEABC'
msg_r = msg.replace('ABC', 'FFF', -1) #第3引数の-1はすべてのでデフォルト　多分何個変換するか的なやつ


msg = 'hello, my name is taro.'
print(msg[:5])
print(msg[1:6])
print(msg[1:6:2]) #一つ飛ばしで取り出す

print(msg.islower()) #islowerですべて小文字ならtrue isupperなら全て大文字でtrue



