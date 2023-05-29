from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/doit', methods=["GET", "POST"])
def doit():
    # 设置页面Content-Type为application/json; charset=utf-8
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response = jsonify()
    # 获取链接中的token值
    token = request.args.get("token")
    # 将值输出到页面json数据
    response.json = {"token": token}
    return response