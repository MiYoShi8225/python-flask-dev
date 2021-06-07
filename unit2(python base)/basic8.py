#セット型
'''
・同じ値を持たない！
・順序が保持されない！
・集合処理を高速化する！
'''

set_a = {'a', 'b', 'c', 'd', 'a', 12} #aが2つあるが実際は1つしか入らない

print(set_a) #実行するタイミングで毎回順番が違う

print('e' in set_a) #'e'がset_aに入っていないのでFalse
print('a' in set_a) #'a'がset_aに入っているのでTrue

print(len(set_a))

# add remove discard pop clear
set_a.add('A')
print(set_a)

set_a.remove('a')
print(set_a)

set_a.discard(12) #discardなら存在しない要素でもエラーにならない！(削除と一緒)
print(set_a)

val = set_a.pop() #ランダムの値がpopされる(システムが任意で選ぶ)
print(val, set_a)

print('\n第二章')
'''
union :和集合(A|B) 両方の合計した集合
intersection :積集合 両方の領域に含まれるもの(A&B) 両方に存在するもの
differende :片方にある集合と片方の集合にない要素を差集合にして返す(A-B)
symmetric_differende :どちらか一方にだけある要素の集合(A^B)
'''


s = {'a' ,'b' ,'c', 'd'}
t = {'c', 'd', 'e', 'f'}

#和集合
u = s|t
u = s.union(t)
print(u)

#積集合
u = s&t
u = s.intersection(t)
print(u)

#差集合
u = s - t
u = s.difference(t)
print(u)

#対象差
u = s ^ t
u = s.symmetric_difference(t)
print(u)


# issubset issuperset isdisjoint
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t)) #sにtの要素が1つでもあるのでTrue
print(s.issuperset(t)) #sの要素がtとすべて一致するとTrue 今回はFalse
print(t.issuperset(s)) #tの要素がsとすべて一致するとTrue 今回はTrue

