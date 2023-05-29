from flask import Flask, jsonify, make_response, request
import requests
import base64
import json

app = Flask(__name__)


@app.route('/doit')
def doit():
    # 创建一个json对象
    json_data = {"status": "error","code": "1001","doit": "INVALID_KEY","callback": "token"}
    # 创建一个响应对象
    response = make_response(jsonify(json_data))
    # 设置响应头
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    # 返回响应对象
    return response