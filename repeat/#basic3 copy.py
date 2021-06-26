# with

class WithTest:

    def __init__(self, filenama):
        print('init called')
        self.__filenama = filenama
    
    def __enter__(self):
        print('enter called')
        self.__filenama = open(self.__filenama, mode='w', encoding='utf-8')
        return self
    
    def write(self, msg):
        self.__filenama.write(msg)
    
    def __exit__(self, exc_type, exc_val, traceback):
        print('exit called')
        self.__filenama.close()
    

with WithTest('./unit2(python base)/unit7/resources/hello.txt') as t:
    print('withの中')
    t.write('test')

