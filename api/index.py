# 导入flask模块
from flask import Flask, request, jsonify
# 创建flask应用对象
app = Flask(__name__)

# 定义一个路由函数，处理根路径的请求
@app.route("/")
def index():
    # 设置页面Content-Type为application/json; charset=utf-8
    response = jsonify()
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    # 获取链接中的token值
    token = request.args.get("token")
    # 将值输出到页面json数据
    response.json = {"token": token}
    return response
