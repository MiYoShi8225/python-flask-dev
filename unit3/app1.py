from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # templatesの中にあるhtmlを呼び出す
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
