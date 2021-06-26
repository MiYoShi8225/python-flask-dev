
animal = "dog"
print(animal)

# 全部大文字になっている変数名は変更してはならない!プログラマーのお約束
LEGAL_AGE = 20

age = 18


if age < LEGAL_AGE:
    print('未成年')
else:
    print('成人')

# format文
print(f'age = {age}') #3.6以降
print(f'{age=}') #3.8以降
