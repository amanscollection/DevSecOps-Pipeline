from flask import Flask, render_template
from flask import request

app = Flask(__name__, template_folder='templates')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['username']
    return f"hello {name}"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return "This is About Page"


if __name__ == '__main__':
    app.run(debug=True)
