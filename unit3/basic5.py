try: #通常処理
    b = [10, 20, 30]
    # c = b[4]
    a = 10/0
    print(b)
except Exception as e: #例外処理
    import traceback
    traceback.print_exc() #こいつ使うとエラー内容を詳細に表示することができる
    #a = 10/0
    print(e)

else: #例外が発生しなかった場合に実行する処理を書く
    print('else処理 例外は発生しませんでした')
    #a = 10 /0

finally: #例外が発生しようとしなかろうと実行する処理を書く
    print('finally elseやexceptでエラーが起きなければ必ず実行される')