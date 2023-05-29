from flask import Flask

app = Flask(__name__)


@app.route('/about')
def about():
    return 'About Page'


@app.route('/doit')
def home():
    return 'Hello, World!'
