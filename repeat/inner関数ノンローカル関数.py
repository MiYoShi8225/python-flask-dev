# inner関数, ノンローカル変数
out_value = None

def outer():
    out_value = '外側の変数'

    def inner():
        nonlocal out_value #外側の関数の変数を書き換える
        out_value = '内側の変数'
        print('inner: outer_value = {}, id = {}'.format(out_value, id(out_value)))
        
    
    inner()
    print('outer: outer_value = {}, id = {}'.format(out_value, id(out_value)))

    def inner2():
        global out_value #globalの関数の変数を書き換える
        out_value = 'globalの変数'
        print('inner2: outer_value = {}, id = {}'.format(out_value, id(out_value)))
    
    inner2()
    print('inner2 after: outer_value = {}, id = {}'.format(out_value, id(out_value)))


outer()

print(out_value)

# nonlocal > global > nomal
