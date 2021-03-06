from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # templatesの中にあるhtmlを呼び出す
    return render_template('index.html')

@app.route('/home/<string:user_name>/<int:age>')
def home(user_name, age):
    login_user = {
        'name': user_name,
        'age': age
    }
    return render_template('home.html', user_info=login_user)

@app.route('/userlist')
def user_list():
    users = [
        'Taro',
        'Jiro',
        'Saburo',
        'Shiro',
        'Hanako'
    ]
    is_login = True
    return render_template('userlist.html', users = users, is_login=is_login)

if __name__ == '__main__':
    app.run(debug=True) #debug機能以外でも変更後の自動更新もやってくれるようになる。
