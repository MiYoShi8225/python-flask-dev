# ファイルへの出力
filepath = './unit2/unit7/resources/input2.csv'

f = open(filepath, mode='w', encoding='utf-8', newline='\n')
f.write('aaa\niii')

f.close()


# with open(filepath, mode='w', encoding='utf-8', newline='\n') as f:
with open(filepath, mode='a', encoding='utf-8', newline='\n') as f:
    list_a = [
        ['A', 'B', 'C'],
        ['あ', 'い', 'う']
    ]
    for x in list_a:
        f.write('\n')
        f.write(','.join(x))
    #f.writelines(''x)