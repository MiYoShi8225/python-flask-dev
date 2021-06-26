'''
:=
セイウチ演算しとして代入と変数の使用を同時にできる！
()で囲む必要がある
'''

if (n := 10) > 5:
    print('nである{}は5より大きい'.format(n))

n = 0
while (n:=n+1) < 10:
    print(n)

print('\n演習')

for i in range(1,101):
    print(i)
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('Buzz')