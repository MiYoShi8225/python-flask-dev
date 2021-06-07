for i in range(5):
    print(i)

for s in ['a', 'b', 'c']:
    print(s)

human = {
    'name': 'Taro',
    'Age': 20,
    'gendar': 'man'
}

for h in human:
    print(h, human[h])

'''
enumerate関数でindex番号を持ってこれる！
'''

#enumerate zip while
print('\n第二章')
fruits = ['greap', 'Pine', 'apple']

for index, value in enumerate(fruits):
    print(index, value)

#zip 配列を2つ同時にループできる

classA = ['taro', 'hanako', 'jiro']
classB = ['katuo', 'wakame', 'taro']

for A,B in zip(classA, classB):
    print('classA student: {}\nclassB student: {}'.format(A, B))

count=0
while count < 10:
    print(count)
    count += 1


print('\n第三章')

for i in range(10):
    if i == 3:
        continue
    elif i == 8:
        #break
        pass
    print(i)
else: #breakでなくfor文が終了した場合はelseの中の処理がはじまる
    print('roop end.')

num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    print(num)
    
else:
    print('while end.')