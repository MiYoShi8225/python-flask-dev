from flask import Flask

# print(__name__)

app = Flask(__name__)

@app.route('/hello')
def hello():
    return '<h1> hello </h1>'

@app.route('/hello/<string:name1>/<string:name2>')
def show_name(name1, name2):
    return '<h1> hello{}, hello,{} </h1>'.format(name1, name2)

@app.route('/add/<int:num1>/<int:num2>')
def add_num(num1, num2):
    return '<h1> {} + {} = {}'.format(num1, num2, num1+num2)

@app.route('/div/<float:num1>/<float:num2>')
def div_num(num1, num2):
    return '<h1> {} '.format(num1 // num2)

if __name__ == '__main__':
    app.run()