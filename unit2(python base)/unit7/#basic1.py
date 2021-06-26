# ファイル入力

filepath = './unit2/unit7/resources/input.csv'

f = open(filepath, mode='r', encoding='utf-8')

# line = f.read() #ファイル全体
# print(line)

# line = f.readlines()
# print(line)
# for x in line:
#     print(x.rstrip('\n'))

# line = f.readline()
# while line:
#     print(line.rstrip('\n'))
#     line = f.readline()
# ↑これと同じことを実施するためセイウチ演算子で補完する

while (line := f.readline()):
    print(line.rstrip('\n'))

f.close()
# ↑メモリ不可を軽減する
#closeは忘れられがちなのでwithを使うことがおおい↓

with open(filepath, mode='r', encoding='utf-8') as f:
    print(f.read())

    #関数の終了でファイルを自動でcloseしている
    