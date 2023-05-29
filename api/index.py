from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/index')
def home():
    return 'This is Home'


@app.route('/about')
def about():
    return 'About'


@app.route('/doit')
def home():
    # 创建一个json对象
    json_data = {
        "status": "error",
        "code": "1001",
        "doit": "INVALID_KEY",
        "callback": "token"
    }
    # 返回json响应
    return jsonify(json_data)
