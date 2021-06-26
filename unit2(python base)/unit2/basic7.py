# dict

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

print(car['brand'])
print(car.get('brand'))

print(car.get('branfd')) #存在しないキーでもNoneを返してくれる

print(car.keys()) #キー一覧
print(car.values()) #値一覧
print(car.items()) #キー+値一覧


for k, v in car.items():
    print('key = {}, value = {}'.format(k, v))

#辞書型メソッド
car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

tmp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}

car.update(tmp_car) #追加と更新
print(car) #modelがprius→カローラに更新されている その他の要素も追加されている

# ↓でも更新とかできる
car['city'] = 'Toyota-shi'
car['year'] = 2017
print(car)

value = car.pop('model')
print(car, value)

car.clear() #中身だけ削除する
print(car)

del car #型すら消すから↓はエラー
print(car)