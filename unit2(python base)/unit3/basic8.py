# global

def printAnimal():
    # 関数内だけ
    #animal = 'cat'

    #関数外にも影響
    global animal
    animal = 'cat'
    
    print('関数内animal = {}, id = {}'.format(animal, id(animal)))

animal = 'Dog'
printAnimal()
print('関数外animal = {}, id = {}'.format(animal, id(animal)))
