#raise 例外自作

class MyException(Exception):
    pass


def devide(a, b):
    if b == 0:
        #raise ZeroDivisionError('0では割り切れません')
        raise MyException('0では割り切れません')
    else:
        return a/b

try:
    c = devide(10 ,0)

except Exception as e:
    print(e ,type(e))

"""
1つめ(現状コメントアウト)
(flaskenv) miyoshishun@miyoshishunnoMacBook-Air python-flask-dev % /Users/miyoshishun/opt/anaconda3/envs/flaskenv/bin/python /Users/miyoshishun/work/python-flask-dev/unit3/basic6.py
0では割り切れません <class 'ZeroDivisionError'>

2つめ
(flaskenv) miyoshishun@miyoshishunnoMacBook-Air python-flask-dev % /Users/miyoshishun/opt/anaconda3/envs/flaskenv/bin/python /Users/miyoshishun/work/python-flask-dev/unit3/basic6.py
0では割り切れません <class '__main__.MyException'>
"""
