# メタクラス

class MetaException:
    pass
    #print('えらーですよ〜')

class Metal(type):
    def __new__(metacls, name, bases, class_dict):
        print('metacls = {}'.format(metacls))
        print('name = {}'.format(name))
        print('bases = {}'.format(bases))
        print('class_dict = {}'.format(class_dict))
        # if 'my_var' not in class_dict.keys():
        #     raise MetaException('my_varを定義してください')
        
        for base in bases:
            if isinstance(base, Metal):
                raise MetaException('継承できません')

        return super().__new__(metacls, name, bases, class_dict)
    
class ClassA(metaclass=Metal):
    a = '123'
    #my_var = 'test'
    pass


class SubClassA(ClassA):
    pass