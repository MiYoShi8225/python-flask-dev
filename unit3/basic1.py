
class ClassA():
    def __init__(self, a):
        self.a = a
    
    def __bool__(self):
        if self.a == 'a':
            return True
        return False



bool_var = ClassA('c')

print('boolの計算結果:{}'.format(bool(bool_var)))

if bool_var:
    print('if文の中の処理')


bool_var = ClassA('a')

print('boolの計算結果:{}'.format(bool(bool_var)))

if bool_var:
    print('if文の中の処理')

print('\n第二章')
# if and or not
msg = 'blue'
msg = 'red'
msg = 'yellow'
if msg == 'blue':
    print('すすめ')
elif msg == 'red':
    print('とまれ')
else:
    print('それ以外の処理')

print('\n2')
age = 10
age = 25
age = 61
if age < 20:
    print('20未満')
elif age <= 40:
    print('20歳以上40歳以下')
elif age >= 60:
    print('60歳以上')
else:
    print('41歳以上60歳未満')

print('\n3')
gender = 'man'
age = 10
if gender == 'man' and age < 20:
    print('未成年男性です')


gender = 'man'
age = 30
if gender == 'man' and age < 20:
    print('未成年男性です')

gender = 'man'
age = 30
if gender == 'man' or age < 20:
    print('未成年または男性もしくは両方です')

print('\n4')
gender = 'woman'
age = 30

#if not gender == 'man':
if gender != 'man':
    print('男ではない')