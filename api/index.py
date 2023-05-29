# 导入flask模块
from flask import Flask, jsonify
# 创建flask应用对象
app = Flask(__name__)

# 定义一个路由函数，处理根路径的请求
@app.route("/doit")
def index():
    # 返回json数据
    return jsonify({"status": "error","code": "1001","doit": "INVALID_KEY","callback": "token"})
