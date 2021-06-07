'''
all any
allはオブジェクトの中身がすべてTrueの場合実施する

anyはオブジェクトの中身が一部でもTrueの場合実施する
'''

#allの中身がすべてTrueであるとTrueを返す
if all((True,10,True,10<20,True)):
    print('allの中の処理')

#allの中身がすべてTrueであるとTrueを返す
if all((True,10,True,10>20,True)): #一部FalseなのでFalseになる
    print('allの中の処理')

#anyの中身は一部でのTrueがあればTrueを返す
if any((False,10,5 == 7,10>20)):
    print('anyの中の処理')

if any((False,10 != 10,5 == 7,10>20)): #全部FalseなのでFalseになる
    print('anyの中の処理')

