from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> hellow world </h1>'

@app.route('/hello')
@app.route('/something') #同一のページを開くこともできる
def hello():
    return '<h2> my hellow world </h2>'

# @app.route('/post/<post_name>') #str型で入力できる
# def show_post(post_name):
#     print(type(post_name))
#     return 'Post {}'.format(post_name)

# @app.route('/post/<int:post_id>') #int型で入力を規制する
# def show_post(post_id):
#     print(type(post_id))
#     return 'Post {}'.format(post_id)

@app.route('/post/<int:post_id>/<post_name>') #2つの引数をとって来ることもできる
def show_post(post_id, post_name):
    # print(type(post_id))
    return '{}: {}'.format(post_name, post_id)

@app.route('/user/<string:user_name>/<int:user_id>')
def show_user(user_name, user_id):
    user_name_id = user_name + str(user_id)
    return '<h1>{}</h1>'.format(user_name_id)

if __name__ == '__main__':
    app.run(debug=True)