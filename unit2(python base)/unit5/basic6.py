
class AllCharacters:

    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('キャラクターはすでに存在しています')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)
    
    @classmethod
    def character_delete(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)

class Character:

    def __init__(self, name, hp, offence, defence):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defence = defence
    
    def attack(self, enemy, critical_point=1):
        if self.hp <= 0:
            print('すでにキャラクターは死んでいます')
            return
        attack_point = self.offence - enemy.defence
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point

        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)
    
    def critical_hit(self, enemy, critical_point = 2):
        if self.hp <= 0:
            print('すでにキャラクターは死んでいます')
            return
        attack_point = self.offence - enemy.defence
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point

        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)

character_a = Character('A', 10, 25, 30)
character_b = Character('b', 10, 30, 20)
character_b = Character('b', 10, 30, 20)

print(AllCharacters.alive_characters)
print(character_b.hp)
character_a.critical_hit(character_b)
print(character_b.hp)
print(AllCharacters.alive_characters)