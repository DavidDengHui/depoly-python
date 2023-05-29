# 导入flask模块
from flask import Flask, jsonify, request
# 创建flask应用对象
app = Flask(__name__)

# 定义一个路由函数，处理根路径的请求
@app.route("/doit")
def index():
    # 获取链接中的token值
    token = request.args.get("token")
    # 将值输出到页面
    return token