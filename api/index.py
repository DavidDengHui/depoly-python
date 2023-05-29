from flask import Flask, jsonify, request
import base64

app = Flask(__name__)


@app.route("/doit")
def doit():
    token = base64.b64decode(request.args.get("token")).decode()
    return jsonify({"status": "error", "code": "1001", "doit": "INVALID_KEY", "callback": token})
