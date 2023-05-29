from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home'


@app.route('/about')
def about():
    return 'About'


@app.route('/doit')
def doit():
    return 'This is API.'
