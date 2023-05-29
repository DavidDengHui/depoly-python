from flask import Flask, jsonify, request
import base64

app = Flask(__name__)


@app.route("/doit")
def index():
    token = base64.b64decode(request.args.get("token")).decode()
    return token
