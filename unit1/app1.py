from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> hellow world </h1>'

@app.route('/hello')
def hello():
    return '<h2> my hellow world </h2>'

if __name__ == '__main__':
    app.run()