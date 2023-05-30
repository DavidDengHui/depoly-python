from flask import Flask, jsonify, request
import re
import base64
import binascii

app = Flask(__name__)


@app.route("/doit")
def doit():
    token = request.args.get("token")
    isb64 = r"^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$"
    if token:
        if token == "get_bili":
            return jsonify({"status": "success", "code": f"{token}", "doit": f"{token}", "callback": f"{token}"})
        else:
            try:
                token = base64.b64decode(token).decode()
                return jsonify({"status": "success", "code": "1101", "doit": f"{token}", "callback": f"{token}"})
            except binascii.Error:
                return jsonify({"status": "error", "code": "1002", "doit": "INVALID_KEY", "callback": f"{token}"})
    else:
        return jsonify({"status": "error", "code": "1001", "doit": "INVALID_KEY", "callback": "NO_KEY"})


if __name__ == '__main__':
    app.run()
