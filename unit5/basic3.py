# コンストラクタ
class SampleClass:
    def __init__(self, msg, name=None): #コンストラクタ
        print('コンストラクタが呼ばれました。')
        self.msg = msg
        self.name = name

    def __del__(self):
        print('delが呼び出されました。')
        print('name = {}'.format(self.name))

    def print_msg(self):
        print(self.msg)
    
    def print_name(self):
        print(self.name)

var_1 = SampleClass('hello', 'Jiro')

var_1.print_msg()
var_1.print_name()
del var_1
# del された後のなので↓は実行エラーになる
var_1.print_name()
