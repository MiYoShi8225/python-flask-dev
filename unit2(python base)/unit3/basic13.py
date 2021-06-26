# じゃんけん　買ったらループの外 3回負けたらループの外

from random import randint

def generator_enemy_hand():
    while True:
        yield '1'
        yield '2'
        yield '3'

def is_win(my_hand, enemy_hand):
    if my_hand == '1' and enemy_hand == '2':
        return True
    if my_hand == '2' and enemy_hand == '3':
        return True
    if my_hand == '3' and enemy_hand == '1':
        return True

lose_count = 0

enemy_hands = generator_enemy_hand()

hand_dict = {
    '1': 'グー',
    '2': 'チョキ',
    '3': 'パー'
}

while True:
    my_hand = str(input('何を出しますか？ 1:グー, 2,チョキ, 3,パー :'))
    if my_hand not in ('1', '2', '3'):
        print('入力が正しくありません')
        continue

    enemy_hand = next(enemy_hands)

    print('あなたの出した手は{}, 相手の出した手は{}'.format(hand_dict[my_hand], hand_dict[enemy_hand]))
    if my_hand == enemy_hand:
        print('あいこ')
    elif is_win(my_hand, enemy_hand):
        print('あなたの勝ち')
        break
    else:
        print('あなたの負け')
        lose_count += 1
        if lose_count == 3:
            print('あなたは負けました。再度チャレンジしてください。')
