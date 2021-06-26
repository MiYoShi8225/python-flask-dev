# lambda 引数:返り値
y = 10

'''
if y > 0:
    return 0
else:
    return 1

↓
'''
x = 0 if y > 0 else 1 #y > 0 => 0 else

#print(x) # 答えは0


lambda_a = lambda x: x * x

print(lambda_a(10))

lambda_b = lambda x, y, z = 5: x*y*z
print(lambda_b(2, 3)) #x=2, y=3, z=5 →30
print(lambda_b(2,3,4)) #x=2, y=3, z=4 →24

#条件式 lambda
lambda_c = lambda x, y: y if x < y else x #xがyよりも小さいならyを返す,そうでないならyを返す
print(lambda_c(2, 4))
print(lambda_c(6, 4))
