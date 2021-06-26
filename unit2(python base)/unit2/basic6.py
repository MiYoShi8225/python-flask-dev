# listのメソッド
list_a = [1, 2, 3, 4, 5]
list_b = list_a[:3]

print(list_b)

#append extend 
list_a.append("apple")
print(list_a)

list_a.append(["banana", "greap"]) #リストの中にリストが追加されちゃう
print(list_a)

list_a.extend(["banana", "greap"]) #リストの中に要素を追加する
print(list_a)

list_a = [1, 2, 3, 4, 5]
list_a.insert(1, "greap") #要素1にgreapを入れる
print(list_a)

# remove pop count index
list_a = [1, 2, 3, 4, 5]
list_a.remove(3)
print(list_a)

value = list_a.pop(2)
print(value, list_a)

print(list_a.index(2))

# sort reverse
list_a = ["banana", "apple", "lemon", "greap"]

print(list_a)

list_a.sort() #アルファベット順
print(list_a)

list_a.reverse() #逆順にする
print(list_a)
