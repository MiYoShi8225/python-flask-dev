list_a = (1, 2, 3, 'a', 4, 'b') #タプル

list_b = [x for x in list_a] #list_aのリスト
print(list_b)

list_b = [x for x in list_a if type(x) == int] #list_aのリスト
print(list_b)

list_c = [x for x in range(100) if x % 7 == 0]
print(list_c)
